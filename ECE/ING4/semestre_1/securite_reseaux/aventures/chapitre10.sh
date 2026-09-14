#!/bin/bash
set -e

echo "[1/5] Nettoyage et préparation..."
systemctl stop openvpn@server 2>/dev/null || true
systemctl stop openvpn-server@server 2>/dev/null || true
rm -rf /etc/openvpn/server/* /etc/openvpn/server.conf /home/florian/openvpn-ca /home/florian/kali.ovpn

echo "[2/5] Initialisation de la PKI et génération des certificats..."
make-cadir /home/florian/openvpn-ca
cd /home/florian/openvpn-ca
./easyrsa init-pki
./easyrsa --batch build-ca nopass
./easyrsa --batch gen-req server nopass
./easyrsa --batch sign-req server server
./easyrsa --batch gen-req kali nopass
./easyrsa --batch sign-req client kali
/usr/sbin/openvpn --genkey secret ta.key

echo "[3/5] Configuration du serveur OpenVPN..."
cp pki/ca.crt pki/issued/server.crt pki/private/server.key ta.key /etc/openvpn/server/

echo "port 1194" > /etc/openvpn/server/server.conf
echo "proto udp" >> /etc/openvpn/server/server.conf
echo "dev tun" >> /etc/openvpn/server/server.conf
echo "ca ca.crt" >> /etc/openvpn/server/server.conf
echo "cert server.crt" >> /etc/openvpn/server/server.conf
echo "key server.key" >> /etc/openvpn/server/server.conf
echo "dh none" >> /etc/openvpn/server/server.conf
echo "topology subnet" >> /etc/openvpn/server/server.conf
echo "server 10.8.0.0 255.255.255.0" >> /etc/openvpn/server/server.conf
echo "ifconfig-pool-persist ipp.txt" >> /etc/openvpn/server/server.conf
echo "push \"redirect-gateway def1 bypass-dhcp\"" >> /etc/openvpn/server/server.conf
echo "keepalive 10 120" >> /etc/openvpn/server/server.conf
echo "tls-crypt ta.key" >> /etc/openvpn/server/server.conf
echo "cipher AES-256-GCM" >> /etc/openvpn/server/server.conf
echo "auth SHA256" >> /etc/openvpn/server/server.conf
echo "persist-key" >> /etc/openvpn/server/server.conf
echo "persist-tun" >> /etc/openvpn/server/server.conf
echo "status openvpn-status.log" >> /etc/openvpn/server/server.conf
echo "verb 3" >> /etc/openvpn/server/server.conf

# Lien symbolique pour compatibilité avec systemd
ln -sf /etc/openvpn/server/server.conf /etc/openvpn/server.conf

echo "[4/5] Démarrage du service OpenVPN..."
systemctl start openvpn-server@server
systemctl enable openvpn-server@server

echo "[5/5] Génération du fichier client /home/florian/kali.ovpn..."
echo "client" > /home/florian/kali.ovpn
echo "dev tun" >> /home/florian/kali.ovpn
echo "proto udp" >> /home/florian/kali.ovpn
echo "remote 192.168.218.128 1194" >> /home/florian/kali.ovpn
echo "resolv-retry infinite" >> /home/florian/kali.ovpn
echo "nobind" >> /home/florian/kali.ovpn
echo "persist-tun" >> /home/florian/kali.ovpn
echo "remote-cert-tls server" >> /home/florian/kali.ovpn
echo "cipher AES-256-GCM" >> /home/florian/kali.ovpn
echo "auth SHA256" >> /home/florian/kali.ovpn
echo "verb 3" >> /home/florian/kali.ovpn

echo "<ca>" >> /home/florian/kali.ovpn
cat /home/florian/openvpn-ca/pki/ca.crt >> /home/florian/kali.ovpn
echo "</ca>" >> /home/florian/kali.ovpn

echo "<cert>" >> /home/florian/kali.ovpn
cat /home/florian/openvpn-ca/pki/issued/kali.crt >> /home/florian/kali.ovpn
echo "</cert>" >> /home/florian/kali.ovpn

echo "<key>" >> /home/florian/kali.ovpn
cat /home/florian/openvpn-ca/pki/private/kali.key >> /home/florian/kali.ovpn
echo "</key>" >> /home/florian/kali.ovpn

echo "<tls-crypt>" >> /home/florian/kali.ovpn
cat /home/florian/openvpn-ca/ta.key >> /home/florian/kali.ovpn
echo "</tls-crypt>" >> /home/florian/kali.ovpn

chown florian:florian /home/florian/kali.ovpn
echo "=== REINSTALLATION COMPLETE ET REUSSIE ==="