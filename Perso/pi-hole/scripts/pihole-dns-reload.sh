#!/usr/bin/env bash
set -Eeuo pipefail

CONTEXT="desktop-linux"
CONTAINER="pihole"
INTERFACE="wlo1"
DNS="127.0.0.1"
PORT="54"

echo "=== Recharge DNS Pi-hole ==="

# Vérifier Docker Desktop
if ! docker --context "$CONTEXT" info >/dev/null 2>&1; then
    echo "ERREUR : Docker Desktop n'est pas disponible."
    exit 1
fi

# Démarrer Pi-hole si nécessaire
RUNNING=$(docker --context "$CONTEXT" inspect \
    -f '{{.State.Running}}' "$CONTAINER" 2>/dev/null || true)

if [[ "$RUNNING" != "true" ]]; then
    echo "Démarrage du conteneur Pi-hole..."
    docker --context "$CONTEXT" start "$CONTAINER" >/dev/null
fi

# Attendre que le DNS réponde
echo "Vérification du DNS..."
READY=false

for i in {1..15}; do
    if dig +time=2 +tries=1 \
        @"$DNS" -p "$PORT" example.com A \
        +short | grep -qE '^[0-9]+\.'; then
        READY=true
        break
    fi
    sleep 2
done

if [[ "$READY" != "true" ]]; then
    echo "ERREUR : Pi-hole ne répond pas correctement."
    echo "Le DNS Fedora n'a pas été modifié."
    exit 1
fi

# Appliquer le DNS Pi-hole à l'interface Wi-Fi
sudo resolvectl dns "$INTERFACE" "$DNS:$PORT"


# Ne pas redémarrer systemd-resolved :
# cela effacerait la configuration DNS temporaire.


echo
echo "=== DNS configuré ==="
resolvectl status "$INTERFACE"

echo
echo "Test de résolution système :"
resolvectl query example.com