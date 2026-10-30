#!/usr/bin/env bash
set -Eeuo pipefail

ACTION="${1:-}"

log() {
    echo "[Pi-hole NetworkManager] $*"
}

die() {
    echo "[ERREUR] $*" >&2
    exit 1
}

[[ $EUID -eq 0 ]] || die "Exécute ce script avec sudo."

command -v ip >/dev/null 2>&1 || die "La commande ip est introuvable."
command -v nmcli >/dev/null 2>&1 || die "NetworkManager (nmcli) est introuvable."
command -v resolvectl >/dev/null 2>&1 || die "systemd-resolved (resolvectl) est introuvable."

detect_interface() {
    local interface

    interface=$(
        ip -4 route get 1.1.1.1 2>/dev/null |
        awk '{for (i=1; i<=NF; i++) if ($i == "dev") {print $(i+1); exit}}'
    )

    if [[ -z "$interface" ]]; then
        interface=$(
            ip -6 route get 2606:4700:4700::1111 2>/dev/null |
            awk '{for (i=1; i<=NF; i++) if ($i == "dev") {print $(i+1); exit}}'
        )
    fi

    [[ -n "$interface" ]] || die "Impossible de détecter l'interface réseau active."
    printf '%s\n' "$interface"
}

get_connection() {
    local interface="$1"
    local connection

    connection=$(nmcli -g GENERAL.CONNECTION device show "$interface" | head -n 1)

    [[ -n "$connection" && "$connection" != "--" ]] ||
        die "Aucun profil NetworkManager actif pour $interface."

    printf '%s\n' "$connection"
}

INTERFACE=$(detect_interface)
CONNECTION=$(get_connection "$INTERFACE")

log "Interface détectée : $INTERFACE"
log "Profil actif : $CONNECTION"

case "$ACTION" in
    enable)
        log "Configuration de Pi-hole comme DNS..."

        resolvectl dns "$INTERFACE" 127.0.0.1
        resolvectl default-route "$INTERFACE" yes
        resolvectl flush-caches

        log "DNS Pi-hole appliqué sur $INTERFACE."
        ;;

    restore)
        log "Restauration du DNS via NetworkManager..."

        nmcli connection up "$CONNECTION" ifname "$INTERFACE"
        resolvectl flush-caches

        log "Profil réseau réactivé : $CONNECTION"
        log "Configuration DNS restaurée."
        ;;

    *)
        die "Action invalide. Utilisation : $0 {enable|restore}"
        ;;
esac
