#!/bin/bash

## Install OpenVPN and Easy-RSA on a Fedora system

sudo dnf install epel-release
sudo dnf install openvpn easy-rsa

mkdir ~/easy-rsa

ln -s /usr/share/easy-rsa/3/* ~/easy-rsa/

sudo chown sammy ~/easy-rsa
chmod 700 ~/easy-rsa



## ICP creation for OpenVPN

sudo dnf install nano
cd ~/easy-rsa
echo "set_var EASYRSA_ALGO "ec" \n set_var EASYRSA_DIGEST "sha512"" > vars

./easyrsa init-pki


## Create the CA and server certificate
cd ~/easy-rsa

./easyrsa gen-req server nopass

sudo cp /home/sammy/easy-rsa/pki/private/server.key /etc/openvpn/server/


## Sign the server certificate with the CA
scp /home/sammy/easy-rsa/pki/reqs/server.req sammy@your_ca_server_ip:/tmp

cd ~/easy-rsa
./easyrsa import-req /tmp/server.req server
./easyrsa sign-req server server

scp pki/issued/server.crt sammy@your_vpn_server_ip:/tmp
scp pki/ca.crt sammy@your_vpn_server_ip:/tmp


sudo cp /tmp/{server.crt,ca.crt} /etc/openvpn/server

## Configuring cryptographic parameters

cd ~/easy-rsa
openvpn --genkey --secret ta.key

sudo cp ta.key /etc/openvpn/server

## Generating client certificates and key pairs
mkdir -p ~/client-configs/keys
chmod -R 700 ~/client-configs

cd ~/easy-rsa
./easyrsa gen-req client1 nopass

cp pki/private/client1.key ~/client-configs/keys/

scp pki/reqs/client1.req sammy@your_ca_server_ip:/tmp

