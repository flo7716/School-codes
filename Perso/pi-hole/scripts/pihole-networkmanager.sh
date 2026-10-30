#!/usr/bin/env bash

set -u

INTERFACE="$1"
ACTION="$2"

PIHOLE_USER="florianandre"
PIHOLE_HOME="/home/florianandre"
CONTAINER="pihole"
DNS="127.0.0.1"
PORT="54"

# Ne traiter que notre interface Wi-Fi
[[ "$INTERFACE" == "wlo1" ]] || exit 0

# Lors d'une déconnexion, retirer la configuration DNS temporaire
if [[ "$ACTION" == "down" || "$ACTION" == "pre-down" ]]; then
    resolvectl revert "$INTERFACE"
    exit 0
fi

# Événements intéressants
[[ "$ACTION" == "up" || "$ACTION" == "dhcp4-change" ]] || exit 0

PIHOLE_UID=$(id -u "$PIHOLE_USER")
RUNTIME_DIR="/run/user/$PIHOLE_UID"

# Exécuter Docker avec l'identité de l'utilisateur
docker_cmd() {
    runuser -u "$PIHOLE_USER" -- \
        env HOME="$PIHOLE_HOME" \
            XDG_RUNTIME_DIR="$RUNTIME_DIR" \
        /usr/bin/docker --context desktop-linux "$@"
}

logger -t pihole-networkmanager \
    "Connexion Wi-Fi détectée : attente de Docker Desktop"

# Attendre Docker Desktop (maximum 120 secondes)
DOCKER_READY=false

for i in {1..60}; do
    if docker_cmd info >/dev/null 2>&1; then
        DOCKER_READY=true
        break
    fi
    sleep 2
done

if [[ "$DOCKER_READY" != "true" ]]; then
    logger -t pihole-networkmanager \
        "Docker Desktop indisponible : restauration du DNS réseau"
    resolvectl revert "$INTERFACE"
    exit 0
fi

# Démarrer Pi-hole si nécessaire
RUNNING=$(docker_cmd inspect \
    -f '{{.State.Running}}' "$CONTAINER" 2>/dev/null || true)

if [[ "$RUNNING" != "true" ]]; then
    logger -t pihole-networkmanager "Démarrage de Pi-hole"

    if ! docker_cmd start "$CONTAINER" >/dev/null; then
        logger -t pihole-networkmanager \
            "Impossible de démarrer Pi-hole"
        resolvectl revert "$INTERFACE"
        exit 0
    fi
fi

# Vérifier que le DNS Pi-hole répond
DNS_READY=false

for i in {1..30}; do
    if dig +time=2 +tries=1 \
        @"$DNS" -p "$PORT" example.com A +short |
        grep -qE '^[0-9]+\.'; then
        DNS_READY=true
        break
    fi
    sleep 2
done

if [[ "$DNS_READY" != "true" ]]; then
    logger -t pihole-networkmanager \
        "Pi-hole ne répond pas : restauration du DNS réseau"
    resolvectl revert "$INTERFACE"
    exit 0
fi

# Appliquer Pi-hole sans redémarrer systemd-resolved
resolvectl dns "$INTERFACE" "$DNS:$PORT"

logger -t pihole-networkmanager \
    "DNS Pi-hole appliqué sur $INTERFACE"
