
#!/usr/bin/env bash
set -Eeuo pipefail

DISPATCHER="/etc/NetworkManager/dispatcher.d/90-pihole-dns"
HELPER="/usr/local/sbin/pihole-networkmanager.sh"
INTERFACE="wlo1"

echo "======================================"
echo " Désinstallation automatisation Pi-hole"
echo "======================================"
echo
echo "Ce script va :"
echo "- Supprimer le déclencheur NetworkManager"
echo "- Supprimer le script DNS automatique"
echo "- Restaurer le DNS réseau sur $INTERFACE"
echo
echo "Les conteneurs et données Pi-hole seront conservés."
echo

read -r -p "Confirmer la suppression ? [y/N] " ANSWER

if [[ ! "$ANSWER" =~ ^[yY]$ ]]; then
    echo "Opération annulée."
    exit 0
fi

# Vérifier les privilèges
if [[ "$EUID" -ne 0 ]]; then
    echo "Relancement avec sudo..."
    exec sudo "$0" "$@"
fi

echo
echo "=== Suppression du déclencheur ==="
if [[ -f "$DISPATCHER" ]]; then
    rm -f "$DISPATCHER"
    echo "Déclencheur NetworkManager supprimé."
else
    echo "Déclencheur déjà absent."
fi

echo
echo "=== Suppression du script DNS ==="
if [[ -f "$HELPER" ]]; then
    rm -f "$HELPER"
    echo "Script DNS supprimé."
else
    echo "Script DNS déjà absent."
fi

echo
echo "=== Restauration du DNS réseau ==="
resolvectl revert "$INTERFACE"

echo
echo "=== Vérification ==="
resolvectl status "$INTERFACE"

echo
echo "======================================"
echo " Automatisation Pi-hole supprimée."
echo "======================================"
echo
echo "Docker Desktop et Pi-hole sont conservés."
echo "Le DNS est désormais géré par NetworkManager."
