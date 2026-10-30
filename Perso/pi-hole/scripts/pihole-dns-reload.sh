#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.yml"
CONTAINER_NAME="pihole"
MAX_ATTEMPTS=30

log() {
    echo "[Pi-hole] $*"
}

die() {
    echo "[ERREUR] $*" >&2
    exit 1
}

[[ $EUID -eq 0 ]] || die "Exécute ce script avec sudo."
command -v docker >/dev/null 2>&1 || die "Docker est introuvable."
command -v dig >/dev/null 2>&1 || die "dig est introuvable. Installe bind-utils."

[[ -f "$COMPOSE_FILE" ]] || die "Fichier Compose introuvable : $COMPOSE_FILE"

log "Démarrage de Pi-hole..."

docker --context default compose \
    --project-directory "$PROJECT_DIR" \
    -f "$COMPOSE_FILE" \
    up -d pihole

log "Attente de la disponibilité DNS..."

for ((attempt=1; attempt<=MAX_ATTEMPTS; attempt++)); do
    if docker --context default inspect "$CONTAINER_NAME" \
        --format '{{.State.Running}}' 2>/dev/null | grep -qx true &&
       dig +time=2 +tries=1 +short @127.0.0.1 example.com | grep -q .; then
        log "Pi-hole répond correctement sur 127.0.0.1:53."
        break
    fi

    if (( attempt == MAX_ATTEMPTS )); then
        die "Pi-hole n'a pas répondu après $MAX_ATTEMPTS tentatives."
    fi

    sleep 2
done

log "Activation de Pi-hole comme DNS système..."

"$SCRIPT_DIR/pihole-networkmanager.sh" enable

log "Pi-hole est opérationnel."
