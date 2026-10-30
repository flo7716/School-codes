#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

[[ $EUID -eq 0 ]] || {
    echo "[ERREUR] Exécute ce script avec sudo." >&2
    exit 1
}

"$SCRIPT_DIR/pihole-networkmanager.sh" restore

echo "[Pi-hole] DNS réseau restauré."
