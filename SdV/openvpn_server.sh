#!/bin/bash

# Script d'installation et de configuration d'OpenVPN sur CentOS 8
# Basé sur : https://www.digitalocean.com/community/tutorials/how-to-set-up-and-configure-an-openvpn-server-on-centos-8-fr

# Vérifier que le script est exécuté en tant que root
if [ "$EUID" -ne 0 ]; then
  echo "Merci d'exécuter ce script en tant que root"
  exit 1
fi

# Variables
VPN_USER="client1"
VPN_PORT="1194"
VPN_PROTOCOL="udp"
VPN_SUBNET="10.8.0.0"
VPN_NETMASK="255.255.255.0"

# 1. Installer les paquets nécessaires
dnf install -y epel-release
dnf install -y openvpn easy-rsa firewalld

# 2. Activer firewalld si nécessaire
systemctl enable firewalld
systemctl start firewalld

# 3. Copier les fichiers Easy-RSA
EASYRSA_DIR=/etc/openvpn/easy-rsa
mkdir -p $EASYRSA_DIR
cp -r /usr/share/easy-rsa/3/* $EASYRSA_DIR
cd $EASYRSA_DIR

# 4. Initialiser PKI
./easyrsa init-pki

# 5. Construire l’autorité de certification (CA)
echo -ne '\n' | ./easyrsa build-ca nopass

# 6. Générer le certificat et la clé du serveur
./easyrsa gen-req server nopass
./easyrsa sign-req server server <<< 'yes'

# 7. Générer les clés Diffie-Hellman
./easyrsa gen-dh

# 8. Générer le certificat du client
./easyrsa gen-req $VPN_USER nopass
./easyrsa sign-req client $VPN_USER <<< 'yes'

# 9. Générer la clé TLS HMAC
openvpn --genkey --secret /etc/openvpn/ta.key

# 10. Copier les certificats et clés
cp pki/ca.crt pki/issued/server.crt pki/private/server.key pki/dh.pem /etc/openvpn/
cp /etc/openvpn/ta.key /etc/openvpn/

# 11. Créer la configuration du serveur
cat > /etc/openvpn/server.conf <<EOF
port $VPN_PORT
proto $VPN_PROTOCOL
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh.pem
auth SHA256
tls-auth ta.key 0
topology subnet
server $VPN_SUBNET $VPN_NETMASK
ifconfig-pool-persist ipp.txt
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 1.1.1.1"
push "dhcp-option DNS 1.0.0.1"
keepalive 10 120
cipher AES-256-CBC
user nobody
group nobody
persist-key
persist-tun
status openvpn-status.log
log-append /var/log/openvpn.log
verb 3
explicit-exit-notify 1
EOF

# 12. Démarrer et activer OpenVPN
systemctl enable openvpn@server
systemctl start openvpn@server

# 13. Activer le routage IPv4
echo 'net.ipv4.ip_forward = 1' >> /etc/sysctl.conf
sysctl -p

# 14. Configurer le pare-feu
firewall-cmd --add-service=openvpn --permanent
firewall-cmd --zone=public --add-masquerade --permanent
firewall-cmd --permanent --add-port=$VPN_PORT/$VPN_PROTOCOL
firewall-cmd --reload

# Ajout de la redirection NAT
IFACE=$(ip route | grep default | awk '{print $5}')
firewall-cmd --permanent --direct --add-rule ipv4 nat POSTROUTING 0 -s $VPN_SUBNET/24 -o $IFACE -j MASQUERADE
firewall-cmd --reload

echo "✅ Installation OpenVPN terminée."
echo "Un client a été généré : $VPN_USER"
