#!/usr/bin/env bash

set -Eeuo pipefail

# ==========================================
# VMware Workstation 17.6.1
# Recompilation des modules vmmon et vmnet
# Fedora Linux
# ==========================================

VMWARE_DIR="$HOME/Documents/vmware-host-modules-17.6.1"
KERNEL="$(uname -r)"

echo "=========================================="
echo " VMware Host Modules - Rebuild"
echo "=========================================="
echo "Noyau actif : $KERNEL"
echo "Dépôt       : $VMWARE_DIR"
echo

# Vérifier les privilèges sudo
sudo -v

# Vérifier le dépôt
if [[ ! -d "$VMWARE_DIR" ]]; then
    echo "[ERREUR] Dépôt VMware introuvable."
    exit 1
fi

cd "$VMWARE_DIR"

# Vérifier les dépendances
echo "[1/6] Vérification des dépendances..."

if ! rpm -q "kernel-devel-$KERNEL" >/dev/null 2>&1; then
    echo "[INFO] Installation de kernel-devel-$KERNEL"
    sudo dnf install -y "kernel-devel-$KERNEL"
fi

for cmd in make gcc perl modinfo; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "[ERREUR] Commande manquante : $cmd"
        exit 1
    fi
done

# Vérifier le répertoire de compilation du noyau
if [[ ! -d "/usr/src/kernels/$KERNEL" ]]; then
    echo "[ERREUR] Sources du noyau introuvables."
    exit 1
fi

# Nettoyage
echo
echo "[2/6] Nettoyage des anciens fichiers compilés..."
make clean

# Compilation
echo
echo "[3/6] Compilation de vmmon et vmnet..."
make -j"$(nproc)"

# Vérification des modules
echo
echo "[4/6] Vérification des modules..."

for module in vmmon vmnet; do
    FILE="$VMWARE_DIR/$module-only/$module.ko"

    if [[ ! -f "$FILE" ]]; then
        echo "[ERREUR] Module absent : $FILE"
        exit 1
    fi

    VERSION="$(modinfo -F vermagic "$FILE" | awk '{print $1}')"

    if [[ "$VERSION" != "$KERNEL" ]]; then
        echo "[ERREUR] Mauvaise version pour $module : $VERSION"
        exit 1
    fi

    echo "[OK] $module compilé pour $VERSION"
done

# Installation
echo
echo "[5/6] Installation des modules..."
sudo make install

# Actualisation des dépendances
sudo depmod -a "$KERNEL"

# Chargement des modules
echo
echo "[6/6] Chargement des modules..."

if lsmod | grep -qE '^vm(mon|net)'; then
    echo "[INFO] Un ou plusieurs modules VMware sont déjà chargés."
    echo "[INFO] Aucun déchargement automatique pour protéger les VM en cours."
    echo "[INFO] Redémarre Fedora pour utiliser les nouveaux modules."
else
    sudo modprobe vmmon
    sudo modprobe vmnet

    if systemctl list-unit-files vmware.service --no-legend |
        grep -q vmware.service; then
        sudo systemctl restart vmware.service
    fi

    echo "[OK] Modules VMware chargés."
fi

echo
echo "=========================================="
echo " Opération terminée !"
echo "=========================================="

echo
echo "Modules installés :"
modinfo -F filename vmmon
modinfo -F filename vmnet

echo
echo "Modules actuellement chargés :"
lsmod | grep -E '^vm(mon|net)' || true