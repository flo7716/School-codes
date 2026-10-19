#!/bin/bash

# Vérification des privilèges root
if [ "$EUID" -ne 0 ]; then
    echo "[-] Veuillez lancer ce script avec sudo ou en tant que root."
    exit 1
fi

SERVER_IP="172.16.130.131"
SHARED_PSK="VotreCleSecretePartagee"

echo "[*] 1. Installation de Libreswan..."
dnf install -y libreswan

echo "[*] 2. Initialisation de la base de données NSS..."
ipsec initnss || echo "[*] Base NSS déjà initialisée, on continue."

echo "[*] 3. Configuration de /etc/ipsec.conf..."
cat << EOF > /etc/ipsec.conf
version 2.0

config setup
    dumpdir=/var/run/pluto
    virtual_private=%v4:10.0.0.0/8,%v4:192.168.0.0/16,%v4:172.16.0.0/12

conn remote-vpn
    keyexchange=ikev2
    left=%defaultroute
    leftsourceip=%config
    leftauth=psk
    right=$SERVER_IP
    rightsubnet=0.0.0.0/0
    rightauth=psk
    auto=start
EOF

echo "[*] 4. Configuration de /etc/ipsec.secrets..."
cat << EOF > /etc/ipsec.secrets
@$SERVER_IP : PSK "$SHARED_PSK"
EOF

echo "[*] 5. Redémarrage du service IPsec..."
systemctl enable --now ipsec.service
systemctl restart ipsec.service

echo "[*] 6. Établissement de la connexion..."
ipsec up remote-vpn

echo "[*] Terminé ! Vérifiez l'état du tunnel avec : sudo ipsec status"