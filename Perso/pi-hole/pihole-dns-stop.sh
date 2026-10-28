#!/usr/bin/env bash
set -Eeuo pipefail

CONTEXT="desktop-linux"
CONTAINER="pihole"
INTERFACE="wlo1"

echo "=== Restauration du DNS Fedora ==="

sudo resolvectl revert "$INTERFACE"

echo
echo "Configuration DNS après restauration :"
resolvectl status "$INTERFACE"

echo
read -r -p "Arrêter le conteneur Pi-hole ? [o/N] " answer

if [[ "$answer" =~ ^[oOyY]$ ]]; then
    docker --context "$CONTEXT" stop "$CONTAINER"
    echo "Pi-hole arrêté."
else
    echo "Pi-hole reste démarré ; le DNS Fedora est restauré."
fi