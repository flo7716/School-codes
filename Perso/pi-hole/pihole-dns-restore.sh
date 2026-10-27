#!/usr/bin/env bash
set -Eeuo pipefail

INTERFACE="wlo1"

echo "=== Restauration DNS automatique Fedora ==="

sudo resolvectl revert "$INTERFACE"

echo
echo "=== DNS actuellement configuré ==="
resolvectl status "$INTERFACE"

echo
echo "=== Test de résolution ==="
resolvectl query example.com