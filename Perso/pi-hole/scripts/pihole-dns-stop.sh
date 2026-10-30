#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.yml"

[[ $EUID -eq 0 ]] || {
    echo "[ERREUR] Exécute ce script avec sudo." >&2
    exit 1
}

[[ -f "$COMPOSE_FILE" ]] || {
    echo "[ERREUR] Fichier Compose introuvable : $COMPOSE_FILE" >&2
    exit 1
}

echo "[Pi-hole] Arrêt du conteneur..."

stop_status=0

docker --context default compose \
    --project-directory "$PROJECT_DIR" \
    -f "$COMPOSE_FILE" \
    stop pihole || stop_status=$?

echo "[Pi-hole] Restauration du DNS réseau..."

restore_status=0

"$SCRIPT_DIR/pihole-dns-restore.sh" || restore_status=$?

if (( stop_status != 0 )); then
    echo "[ERREUR] L'arrêt de Pi-hole a échoué." >&2
fi

if (( restore_status != 0 )); then
    echo "[ERREUR] La restauration DNS a échoué." >&2
fi

if (( stop_status != 0 || restore_status != 0 )); then
    exit 1
fi

echo "[Pi-hole] Arrêt terminé. DNS réseau restauré."
