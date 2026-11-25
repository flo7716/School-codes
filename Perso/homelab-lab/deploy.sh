#!/usr/bin/env bash
# Déploiement du labo homelab.
# Usage : ./deploy.sh [up|down|reset|status|tunnel|trust-ca|nextcloud-domain|test|logs [service]]
set -euo pipefail
cd "$(dirname "$0")"

SECRETS_DIR="$PWD/secrets"
KEY="$SECRETS_DIR/lab_ed25519"
SSH_CFG="$PWD/ssh_config"

c_ok()   { printf '\033[32m%s\033[0m\n' "$*"; }
c_warn() { printf '\033[33m%s\033[0m\n' "$*"; }
c_err()  { printf '\033[31m%s\033[0m\n' "$*" >&2; }

require() {
    command -v docker >/dev/null || { c_err "Docker introuvable."; exit 1; }
    docker compose version >/dev/null 2>&1 || { c_err "Docker Compose v2 requis (docker compose)."; exit 1; }
    command -v ssh-keygen >/dev/null || { c_err "ssh-keygen introuvable (paquet openssh-client)."; exit 1; }
}

randpw() { LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 24; }

init_secrets() {
    mkdir -p "$SECRETS_DIR"
    chmod 700 "$SECRETS_DIR"

    if [[ ! -f .env ]]; then
        umask 077
        cat > .env <<EOF
# Généré par deploy.sh le $(date -Iseconds) — ne pas versionner
BIND_IP=127.0.0.1
SSH_PUBLIC_PORT=2222
HTTPS_PUBLIC_PORT=443
NEXTCLOUD_DOMAIN=nextcloud.localhost
PIHOLE_PASSWORD=$(randpw)
MARIADB_ROOT_PASSWORD=$(randpw)
MARIADB_PASSWORD=$(randpw)
REDIS_PASSWORD=$(randpw)
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=$(randpw)
EOF
        c_ok "Fichier .env créé avec des mots de passe aléatoires."
    fi
    # .env créé par une version précédente du labo : on complète
    grep -q '^BIND_IP=' .env           || echo 'BIND_IP=127.0.0.1' >> .env
    grep -q '^HTTPS_PUBLIC_PORT=' .env || echo 'HTTPS_PUBLIC_PORT=443' >> .env
    grep -q '^NEXTCLOUD_DOMAIN=' .env  || echo 'NEXTCLOUD_DOMAIN=nextcloud.localhost' >> .env

    if [[ ! -f "$KEY" ]]; then
        ssh-keygen -q -t ed25519 -N '' -C "homelab-lab" -f "$KEY"
        c_ok "Clé SSH du labo créée : $KEY"
    fi

    local port host
    port=$(grep -E '^SSH_PUBLIC_PORT=' .env | cut -d= -f2)
    host=$(grep -E '^BIND_IP=' .env | cut -d= -f2)
    [[ -z "$host" || "$host" == 0.0.0.0 ]] && host=127.0.0.1
    cat > "$SSH_CFG" <<EOF
# Généré par deploy.sh — usage : ssh -F ssh_config lab-bastion
Host lab-bastion
    HostName ${host}
    Port ${port:-2222}
    User admin
    IdentityFile $KEY
    IdentitiesOnly yes
    UserKnownHostsFile $SECRETS_DIR/known_hosts
    StrictHostKeyChecking accept-new
EOF
}

print_access() {
    # shellcheck disable=SC1091
    source .env
    local url="https://$NEXTCLOUD_DOMAIN"
    [[ "$HTTPS_PUBLIC_PORT" != 443 ]] && url="$url:$HTTPS_PUBLIC_PORT"
    cat <<EOF

$(c_ok "Labo démarré.")
  Nextcloud    : $url   ($NEXTCLOUD_ADMIN_USER / $NEXTCLOUD_ADMIN_PASSWORD)
                 -> navigateur, ou GNOME : Paramètres > Comptes en ligne > Nextcloud
                 -> 1re fois : ./deploy.sh trust-ca  (faire confiance au certificat)
  Admin (SSH)  : ssh -F ssh_config lab-bastion
                 ./deploy.sh tunnel  -> Pi-hole : http://localhost:8080/admin (mdp : $PIHOLE_PASSWORD)
                                        Cockpit : https://localhost:9090 (si installé sur l'hôte)
  Tests        : ./deploy.sh test    (Nextcloud met 1 à 2 min à s'installer au 1er lancement)
  Mots de passe: fichier .env
EOF
}

cmd="${1:-up}"
case "$cmd" in
    up)
        require
        init_secrets
        docker compose up -d --build
        print_access
        ;;
    down)
        docker compose down
        ;;
    reset)
        read -r -p "Supprimer conteneurs, volumes (données Nextcloud/Pi-hole), .env et secrets ? [o/N] " a
        if [[ "$a" =~ ^[oOyY]$ ]]; then
            docker compose down -v --remove-orphans
            rm -rf "$SECRETS_DIR" .env "$SSH_CFG"
            c_ok "Labo réinitialisé."
        else
            echo "Annulé."
        fi
        ;;
    status)
        docker compose ps
        ;;
    tunnel)
        c_warn "Tunnels admin ouverts (Ctrl+C pour fermer) :"
        c_warn "  Pi-hole -> http://localhost:8080/admin"
        c_warn "  Cockpit -> https://localhost:9090   (hôte, si host/setup-host.sh a été lancé)"
        exec ssh -F "$SSH_CFG" -N \
            -L 8080:10.10.10.10:80 \
            -L 9090:10.10.20.1:9090 \
            lab-bastion
        ;;
    trust-ca)
        # Exporte la CA interne de Caddy et l'ajoute au magasin système du laptop
        mkdir -p "$SECRETS_DIR"
        docker cp lab-proxy:/data/caddy/pki/authorities/local/root.crt "$SECRETS_DIR/homelab-ca.crt"
        c_ok "CA exportée : $SECRETS_DIR/homelab-ca.crt"
        if [[ -d /etc/pki/ca-trust/source/anchors ]]; then          # Fedora / RHEL / Rocky
            sudo cp "$SECRETS_DIR/homelab-ca.crt" /etc/pki/ca-trust/source/anchors/homelab-ca.crt
            sudo update-ca-trust
        elif [[ -d /usr/local/share/ca-certificates ]]; then        # Debian / Ubuntu
            sudo cp "$SECRETS_DIR/homelab-ca.crt" /usr/local/share/ca-certificates/homelab-ca.crt
            sudo update-ca-certificates
        else
            c_warn "Distribution non reconnue : ajoute $SECRETS_DIR/homelab-ca.crt au magasin de certificats à la main."
        fi
        if command -v certutil >/dev/null && [[ -d "$HOME/.pki/nssdb" ]]; then   # Chrome / Chromium
            certutil -d "sql:$HOME/.pki/nssdb" -A -t "C,," -n homelab-ca -i "$SECRETS_DIR/homelab-ca.crt"
        fi
        c_ok "CA installée pour le système (GNOME, curl, Chrome si certutil est présent)."
        # Nom -> IP en IPv4 explicite (sinon *.localhost peut partir sur ::1, non publié)
        # shellcheck disable=SC1091
        source .env
        local_ip=${BIND_IP:-127.0.0.1}; [[ "$local_ip" == 0.0.0.0 ]] && local_ip=127.0.0.1
        if ! grep -qE "^[0-9.]+[[:space:]]+${NEXTCLOUD_DOMAIN//./\\.}([[:space:]]|$)" /etc/hosts; then
            echo "$local_ip  $NEXTCLOUD_DOMAIN" | sudo tee -a /etc/hosts >/dev/null
            c_ok "/etc/hosts : $NEXTCLOUD_DOMAIN -> $local_ip"
        fi
        c_warn "Firefox : about:config -> security.enterprise_roots.enabled = true, ou importer le .crt dans Paramètres > Certificats."
        ;;
    nextcloud-domain)
        # Ajoute NEXTCLOUD_DOMAIN aux domaines approuvés d'une instance déjà installée
        # shellcheck disable=SC1091
        source .env
        docker exec -u www-data lab-nextcloud php occ config:system:set trusted_domains 0 --value="$NEXTCLOUD_DOMAIN"
        docker exec -u www-data lab-nextcloud php occ config:system:set trusted_domains 1 --value=10.10.10.20
        docker exec -u www-data lab-nextcloud php occ config:system:set overwrite.cli.url --value="https://$NEXTCLOUD_DOMAIN"
        c_ok "Domaines approuvés mis à jour."
        ;;
    test)
        exec ./test.sh
        ;;
    logs)
        shift
        docker compose logs -f --tail=100 "$@"
        ;;
    *)
        echo "Usage : $0 [up|down|reset|status|tunnel|trust-ca|nextcloud-domain|test|logs [service]]"
        exit 1
        ;;
esac
