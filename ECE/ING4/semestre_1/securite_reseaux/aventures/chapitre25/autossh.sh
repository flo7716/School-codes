#!/bin/bash

# Vérifier si l'IP est passée en argument
if [ -z "$1" ]; then
    echo "Usage: $0 <IP_SERVEUR>"
    exit 1
fi

REMOTE_IP=$1
REMOTE_USER="user" # Adaptez si besoin

# 1. Générer la clé automatiquement sans passphrase (-N "") et écraser l'ancienne si elle existe (-f)
echo "[+] Génération de la paire de clés SSH..."
ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa -q

# 2. Copier la clé sur le serveur distant
# Note: ssh-copy-id va demander le mot de passe de l'utilisateur distant une dernière fois.
echo "[+] Copie de la clé publique sur le serveur $REMOTE_IP..."
ssh-copy-id -o StrictHostKeyChecking=no $REMOTE_USER@$REMOTE_IP

echo "[+] Terminé ! Vous pouvez désormais vous connecter sans mot de passe :"
echo "ssh $REMOTE_USER@$REMOTE_IP"
