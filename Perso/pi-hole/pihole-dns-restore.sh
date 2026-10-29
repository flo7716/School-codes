#!/usr/bin/env bash
set -Eeuo pipefail

INTERFACE="wlo1"

echo "=== Restauration DNS automatique Fedora ==="

sudo resolvectl revert "$INTERFACE"

echo
echo "=== DNS actuellement configuré ==="
resolvectl status "$INTERFACE"

# redémarrage du service systemd-resolved pour appliquer les changements
sudo systemctl restart systemd-resolved

echo
echo "=== Test de résolution ==="
resolvectl query example.com