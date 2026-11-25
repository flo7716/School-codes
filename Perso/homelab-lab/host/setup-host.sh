#!/usr/bin/env bash
# =============================================================================
#  Préparation de l'hôte (hyperviseur) AlmaLinux / Rocky 9-10 — aussi Fedora
#    - Docker Engine natif + plugin compose
#    - KVM / libvirt (pour les futures VMs)
#    - Cockpit (hôte, stockage, VMs, SELinux), joignable UNIQUEMENT
#      depuis le réseau admin du labo, donc via le bastion
#
#  Usage : sudo ./host/setup-host.sh
#  Idempotent : peut être relancé sans casse.
# =============================================================================
set -euo pipefail

ADMIN_HOST_IP="10.10.20.1"   # IP de l'hôte sur le réseau Docker "admin"
COCKPIT_PORT="9090"

ok()   { printf '\033[32m✔ %s\033[0m\n' "$*"; }
info() { printf '\033[36m→ %s\033[0m\n' "$*"; }
warn() { printf '\033[33m! %s\033[0m\n' "$*"; }
die()  { printf '\033[31m✘ %s\033[0m\n' "$*" >&2; exit 1; }

[[ $EUID -eq 0 ]] || die "À lancer avec sudo."

# shellcheck disable=SC1091
. /etc/os-release
case "$ID" in
    almalinux|rocky|rhel) DOCKER_REPO="https://download.docker.com/linux/rhel/docker-ce.repo" ;;
    fedora)               DOCKER_REPO="https://download.docker.com/linux/fedora/docker-ce.repo" ;;
    *) die "Distribution non prise en charge : $ID" ;;
esac
info "Système : $PRETTY_NAME"

# ------------------------------------------------------------ vérifications --
if grep -qE 'vmx|svm' /proc/cpuinfo; then
    ok "Virtualisation matérielle (VT-x/AMD-V) disponible"
else
    warn "VT-x absent ou désactivé dans le BIOS : les VMs KVM ne fonctionneront pas"
fi
[[ "$(getenforce 2>/dev/null || echo Disabled)" == Enforcing ]] \
    && ok "SELinux : Enforcing" \
    || warn "SELinux n'est pas en mode Enforcing (recommandé : laisser Enforcing)"

# ------------------------------------------------------------------ Docker --
if rpm -q podman-docker &>/dev/null; then
    info "Suppression de podman-docker (conflit avec la commande docker)"
    dnf -y remove podman-docker
fi
if ! rpm -q docker-ce &>/dev/null; then
    info "Installation de Docker Engine"
    dnf -y install dnf-plugins-core
    if [[ ! -f /etc/yum.repos.d/docker-ce.repo ]]; then
        curl -fsSL "$DOCKER_REPO" -o /etc/yum.repos.d/docker-ce.repo
    fi
    dnf -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
fi

mkdir -p /etc/docker
if [[ ! -f /etc/docker/daemon.json ]]; then
    cat > /etc/docker/daemon.json <<'EOF'
{
  "log-driver": "json-file",
  "log-opts": { "max-size": "10m", "max-file": "3" },
  "live-restore": true
}
EOF
    ok "daemon.json : rotation des logs + live-restore"
else
    warn "/etc/docker/daemon.json existe déjà : non modifié"
fi
systemctl enable --now docker
ok "Docker $(docker version --format '{{.Server.Version}}') actif"

# ------------------------------------------------------------ KVM / libvirt --
info "Installation de KVM / libvirt"
dnf -y install qemu-kvm libvirt virt-install
# Démons libvirt modulaires (recommandés sur EL9+, Fedora)
for drv in qemu network nodedev nwfilter secret storage interface; do
    systemctl enable --now "virt${drv}d.socket" 2>/dev/null || true
done
ok "libvirt prêt (réseau par défaut virbr0 192.168.122.0/24)"

# ----------------------------------------------------------------- Cockpit --
info "Installation de Cockpit"
dnf -y install cockpit cockpit-machines cockpit-storaged cockpit-selinux
dnf -y install cockpit-files 2>/dev/null || true   # selon la version de la distribution

# Écoute UNIQUEMENT sur l'IP de l'hôte côté réseau admin.
# FreeBind : le socket démarre même si le bridge Docker n'existe pas encore.
mkdir -p /etc/systemd/system/cockpit.socket.d
cat > /etc/systemd/system/cockpit.socket.d/listen.conf <<EOF
[Socket]
ListenStream=
ListenStream=${ADMIN_HOST_IP}:${COCKPIT_PORT}
FreeBind=yes
EOF

cat > /etc/cockpit/cockpit.conf <<EOF
[WebService]
# Accès via le tunnel SSH du bastion : https://localhost:9090
Origins = https://localhost:${COCKPIT_PORT} https://127.0.0.1:${COCKPIT_PORT}
LoginTitle = Homelab — hyperviseur

[Session]
IdleTimeout = 15
EOF

# root interdit dans Cockpit (c'est déjà le défaut, on s'en assure)
grep -qx root /etc/cockpit/disallowed-users 2>/dev/null || echo root >> /etc/cockpit/disallowed-users

systemctl daemon-reload
systemctl enable cockpit.socket
systemctl restart cockpit.socket
ok "Cockpit écoute sur ${ADMIN_HOST_IP}:${COCKPIT_PORT} uniquement"

# --------------------------------------------------------------- firewalld --
if systemctl is-active --quiet firewalld; then
    zone=$(firewall-cmd --get-default-zone)
    if firewall-cmd --zone="$zone" --query-service=cockpit &>/dev/null; then
        firewall-cmd --permanent --zone="$zone" --remove-service=cockpit
        firewall-cmd --reload
        ok "firewalld : Cockpit retiré de la zone '$zone' (plus exposé sur le LAN)"
    else
        ok "firewalld : Cockpit n'est pas ouvert dans la zone '$zone'"
    fi
else
    warn "firewalld inactif : recommandé sur l'hôte (systemctl enable --now firewalld)"
fi

# ------------------------------------------------------- compte d'admin --
admin_user="${SUDO_USER:-}"
if [[ -n "$admin_user" && "$admin_user" != root ]]; then
    if ! id -nG "$admin_user" | grep -qw wheel; then
        usermod -aG wheel "$admin_user"
        ok "$admin_user ajouté au groupe wheel (administration dans Cockpit)"
    fi
    if ! id -nG "$admin_user" | grep -qw libvirt; then
        usermod -aG libvirt "$admin_user"
        ok "$admin_user ajouté au groupe libvirt (VMs dans Cockpit)"
    fi
    warn "Pas d'ajout au groupe docker (équivalent root) : utiliser sudo pour docker."
fi

cat <<EOF

$(ok "Hôte prêt.")
  1. Lancer le labo     : ./deploy.sh   (crée le réseau admin ${ADMIN_HOST_IP})
  2. Ouvrir les tunnels : ./deploy.sh tunnel   (depuis ton laptop)
  3. Cockpit            : https://localhost:${COCKPIT_PORT}
                          (certificat auto-signé de Cockpit : avertissement normal)
  Connexion avec ton compte Linux de l'hôte (mot de passe), pas root.
EOF
