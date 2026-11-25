#!/usr/bin/env bash
# =============================================================================
#  VM AlmaLinux "hyperviseur" sur le laptop Fedora — répétition du M920x
#
#  ./host/vm.sh create    crée la VM (installation automatique, ~10 min)
#  ./host/vm.sh push      copie le projet dans la VM
#  ./host/vm.sh deploy    dans la VM : setup-host.sh (Docker, KVM, Cockpit) + labo
#  ./host/vm.sh access    récupère clé du bastion + CA, configure le laptop
#  ./host/vm.sh tunnel    tunnels admin : Pi-hole :8080, Cockpit d'Alma :9090
#  ./host/vm.sh all       create + push + deploy + access
#  ./host/vm.sh ip | ssh | test | stop | start | destroy
#
#  Variables (optionnelles) : VM_NAME, VM_RAM (Mo), VM_CPUS, VM_DISK (Go),
#                             ALMA_VERSION (9 par défaut), NC_DOMAIN
# =============================================================================
set -euo pipefail

PROJECT=$(cd "$(dirname "$0")/.." && pwd)
ACCESS="$PROJECT/vm-access"
VM_NAME=${VM_NAME:-alma-hv}
VM_RAM=${VM_RAM:-6144}
VM_CPUS=${VM_CPUS:-4}
VM_DISK=${VM_DISK:-40}
ALMA_VERSION=${ALMA_VERSION:-9}
NC_DOMAIN=${NC_DOMAIN:-nextcloud.home.arpa}
VM_USER=${USER}
REPO="https://repo.almalinux.org/almalinux/${ALMA_VERSION}"
VIRSH=(sudo virsh -c qemu:///system)
SSH=(ssh -F "$ACCESS/ssh_config")

ok()   { printf '\033[32m✔ %s\033[0m\n' "$*"; }
info() { printf '\033[36m→ %s\033[0m\n' "$*"; }
warn() { printf '\033[33m! %s\033[0m\n' "$*"; }
die()  { printf '\033[31m✘ %s\033[0m\n' "$*" >&2; exit 1; }
# Plus jamais d'arrêt silencieux : on affiche la ligne et la commande en échec
trap 'printf "\033[31m✘ Échec ligne %s : %s\033[0m\n" "$LINENO" "$BASH_COMMAND" >&2' ERR

vm_ip() {
    "${VIRSH[@]}" domifaddr "$VM_NAME" --source lease 2>/dev/null \
        | awk '/ipv4/ { split($4, a, "/"); print a[1] }' | head -n1 || true
}

wait_ip() {
    local ip=""
    for _ in $(seq 1 60); do
        ip=$(vm_ip); [[ -n "$ip" ]] && { echo "$ip"; return; }
        sleep 3
    done
    die "Impossible d'obtenir l'IP de la VM (virsh domifaddr $VM_NAME)"
}

write_ssh_config() {
    local ip=$1 key=$2
    cat > "$ACCESS/ssh_config" <<EOF
# Généré par host/vm.sh
Host $VM_NAME
    HostName $ip
    User $VM_USER
    IdentityFile $key
    IdentitiesOnly yes
    UserKnownHostsFile $ACCESS/known_hosts
    StrictHostKeyChecking accept-new

Host vm-bastion
    HostName $ip
    Port 2222
    User admin
    IdentityFile $ACCESS/lab_ed25519
    IdentitiesOnly yes
    UserKnownHostsFile $ACCESS/known_hosts
    StrictHostKeyChecking accept-new
EOF
}

# --------------------------------------------------------------------------
cmd_create() {
    command -v virt-install >/dev/null || {
        info "Installation des outils de virtualisation (Fedora)"
        sudo dnf -y install @virtualization
    }
    sudo systemctl enable --now libvirtd 2>/dev/null || sudo systemctl enable --now virtqemud.socket
    "${VIRSH[@]}" net-start default 2>/dev/null || true
    "${VIRSH[@]}" net-autostart default >/dev/null 2>&1 || true
    "${VIRSH[@]}" dominfo "$VM_NAME" &>/dev/null && die "La VM $VM_NAME existe déjà (./host/vm.sh destroy pour repartir de zéro)"

    mkdir -p "$ACCESS"; chmod 700 "$ACCESS"

    # Clé SSH pour se connecter à la VM : celle du laptop si elle existe
    local pub key
    if [[ -f "$HOME/.ssh/id_ed25519.pub" ]]; then
        key="$HOME/.ssh/id_ed25519"
    else
        key="$ACCESS/vm_ed25519"
        [[ -f "$key" ]] || ssh-keygen -q -t ed25519 -N '' -C "alma-hv" -f "$key"
    fi
    pub=$(cat "$key.pub")

    # Mot de passe du compte (sudo + Cockpit), stocké en local
    local pw hash
    pw=$(head -c 512 /dev/urandom | LC_ALL=C tr -dc 'A-Za-z0-9' | head -c 16)
    hash=$(openssl passwd -6 "$pw")
    umask 077; echo "$pw" > "$ACCESS/vm-password.txt"; umask 022

    local tmp; tmp=$(mktemp -d)
    cat > "$tmp/ks.cfg" <<EOF
# Kickstart AlmaLinux ${ALMA_VERSION} — hyperviseur du homelab
text
url --url=${REPO}/BaseOS/x86_64/os/
repo --name=AppStream --baseurl=${REPO}/AppStream/x86_64/os/
lang fr_FR.UTF-8
keyboard --vckeymap=fr --xlayouts='fr'
timezone Europe/Paris --utc
network --bootproto=dhcp --hostname=${VM_NAME} --activate
rootpw --lock
user --name=${VM_USER} --groups=wheel --password=${hash} --iscrypted
sshkey --username=${VM_USER} "${pub}"
selinux --enforcing
firewall --enabled --service=ssh
bootloader --append="console=ttyS0,115200n8"
zerombr
clearpart --all --initlabel
autopart --type=lvm --nohome
%packages
@^minimal-environment
tar
openssl
%end
poweroff
EOF

    info "Installation d'AlmaLinux ${ALMA_VERSION} dans la VM $VM_NAME (${VM_RAM} Mo, ${VM_CPUS} vCPU, ${VM_DISK} Go)"
    info "Téléchargement depuis repo.almalinux.org : compter 10 à 20 minutes."
    sudo virt-install --connect qemu:///system \
        --name "$VM_NAME" --memory "$VM_RAM" --vcpus "$VM_CPUS" \
        --cpu host-passthrough \
        --disk "size=${VM_DISK},format=qcow2" \
        --os-variant "almalinux${ALMA_VERSION}" \
        --network network=default \
        --location "${REPO}/BaseOS/x86_64/os/" \
        --initrd-inject "$tmp/ks.cfg" \
        --extra-args "inst.ks=file:/ks.cfg console=ttyS0,115200n8" \
        --graphics none --noautoconsole --noreboot --wait -1
    rm -rf "$tmp"

    "${VIRSH[@]}" start "$VM_NAME" >/dev/null
    "${VIRSH[@]}" autostart "$VM_NAME" >/dev/null
    local ip; ip=$(wait_ip)
    write_ssh_config "$ip" "$key"

    info "Attente de SSH sur $ip"
    for _ in $(seq 1 40); do
        "${SSH[@]}" -o ConnectTimeout=3 -o BatchMode=yes "$VM_NAME" true 2>/dev/null && break
        sleep 3
    done
    ok "VM prête : $ip — ssh -F vm-access/ssh_config $VM_NAME"
    ok "Mot de passe de $VM_USER (sudo, Cockpit) : vm-access/vm-password.txt"
}

cmd_push() {
    info "Copie du projet dans la VM (~/homelab-lab)"
    tar -C "$PROJECT" --exclude=./.env --exclude=./secrets --exclude=./vm-access \
        --exclude=./ssh_config -czf - . \
        | "${SSH[@]}" "$VM_NAME" 'mkdir -p ~/homelab-lab && tar -xzf - -C ~/homelab-lab'
    ok "Projet copié"
}

cmd_deploy() {
    local ip; ip=$(vm_ip); [[ -n "$ip" ]] || die "VM éteinte ? (./host/vm.sh start)"
    info "Dans la VM : préparation de l'hôte puis déploiement du labo"
    warn "Mot de passe sudo demandé : $(cat "$ACCESS/vm-password.txt")"
    "${SSH[@]}" -t "$VM_NAME" "set -e; cd ~/homelab-lab
        sudo ./host/setup-host.sh
        sudo BIND_IP=$ip NEXTCLOUD_DOMAIN=$NC_DOMAIN ./deploy.sh
        for i in \$(seq 1 30); do
            sudo docker cp lab-proxy:/data/caddy/pki/authorities/local/root.crt secrets/homelab-ca.crt 2>/dev/null && break
            sleep 2
        done
        sudo chown -R \"\$USER:\" .env secrets ssh_config"
    ok "Labo déployé dans la VM"
}

cmd_access() {
    local ip; ip=$(vm_ip); [[ -n "$ip" ]] || die "VM éteinte ?"
    info "Récupération de la clé du bastion et de la CA du labo"
    scp -F "$ACCESS/ssh_config" -q "$VM_NAME:homelab-lab/secrets/lab_ed25519" "$ACCESS/lab_ed25519"
    scp -F "$ACCESS/ssh_config" -q "$VM_NAME:homelab-lab/secrets/homelab-ca.crt" "$ACCESS/homelab-vm-ca.crt"
    chmod 600 "$ACCESS/lab_ed25519"

    # Nom de Nextcloud -> IP de la VM
    if grep -qE "[[:space:]]${NC_DOMAIN//./\\.}([[:space:]]|$)" /etc/hosts; then
        sudo sed -i "/[[:space:]]${NC_DOMAIN//./\\.}\([[:space:]]\|$\)/d" /etc/hosts
    fi
    echo "$ip  $NC_DOMAIN" | sudo tee -a /etc/hosts >/dev/null
    ok "/etc/hosts : $NC_DOMAIN -> $ip"

    # Confiance dans la CA du labo (Fedora)
    sudo cp "$ACCESS/homelab-vm-ca.crt" /etc/pki/ca-trust/source/anchors/homelab-vm-ca.crt
    sudo update-ca-trust
    if command -v certutil >/dev/null && [[ -d "$HOME/.pki/nssdb" ]]; then
        certutil -d "sql:$HOME/.pki/nssdb" -D -n homelab-vm-ca 2>/dev/null || true
        certutil -d "sql:$HOME/.pki/nssdb" -A -t "C,," -n homelab-vm-ca -i "$ACCESS/homelab-vm-ca.crt"
    fi
    ok "CA du labo installée (système, GNOME, Chrome)"
    warn "Firefox : about:config -> security.enterprise_roots.enabled = true"
    cat <<EOF

  Nextcloud     : https://$NC_DOMAIN   (identifiants : ssh -F vm-access/ssh_config $VM_NAME 'grep NEXTCLOUD homelab-lab/.env')
  Admin (SSH)   : ssh -F vm-access/ssh_config vm-bastion
  Tunnels admin : ./host/vm.sh tunnel  -> Pi-hole http://localhost:8080/admin
                                          Cockpit AlmaLinux https://localhost:9090
                  Cockpit : utilisateur $VM_USER, mot de passe dans vm-access/vm-password.txt
EOF
}

cmd_tunnel() {
    warn "Tunnels via le bastion de la VM (Ctrl+C pour fermer) :"
    warn "  Pi-hole -> http://localhost:8080/admin"
    warn "  Cockpit AlmaLinux -> https://localhost:9090"
    exec "${SSH[@]}" -N -L 8080:10.10.10.10:80 -L 9090:10.10.20.1:9090 vm-bastion
}

cmd_test() {
    "${SSH[@]}" -t "$VM_NAME" 'cd ~/homelab-lab && sudo ./test.sh'
    info "Depuis le laptop :"
    if curl -sf --max-time 5 "https://$NC_DOMAIN/status.php" | grep -q '"installed":true'; then
        ok "https://$NC_DOMAIN répond, certificat reconnu"
    else
        warn "https://$NC_DOMAIN ne répond pas depuis le laptop (lancer ./host/vm.sh access ?)"
    fi
}

case "${1:-}" in
    create)  cmd_create ;;
    push)    cmd_push ;;
    deploy)  cmd_deploy ;;
    access)  cmd_access ;;
    tunnel)  cmd_tunnel ;;
    test)    cmd_test ;;
    all)     cmd_create; cmd_push; cmd_deploy; cmd_access ;;
    ip)      vm_ip ;;
    ssh)     shift; exec "${SSH[@]}" "$VM_NAME" "$@" ;;
    start)   "${VIRSH[@]}" start "$VM_NAME" ;;
    stop)    "${VIRSH[@]}" shutdown "$VM_NAME" ;;
    destroy)
        read -r -p "Supprimer définitivement la VM $VM_NAME et son disque ? [o/N] " a
        [[ "$a" =~ ^[oOyY]$ ]] || { echo "Annulé."; exit 0; }
        "${VIRSH[@]}" destroy "$VM_NAME" 2>/dev/null || true
        "${VIRSH[@]}" undefine "$VM_NAME" --remove-all-storage
        rm -f "$ACCESS/ssh_config" "$ACCESS/known_hosts" "$ACCESS/vm-password.txt"
        ok "VM supprimée"
        ;;
    *) sed -n '3,15p' "$0" | sed 's/^#  \{0,1\}//'; exit 1 ;;
esac
