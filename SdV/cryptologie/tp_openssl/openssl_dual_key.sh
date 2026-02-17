#!/bin/bash

# Générer une paire de clés OpenSSL
openssl genpkey -algorithm RSA -out private_key_generated.pem -pkeyopt rsa_keygen_bits:2048

# Extraire la clé publique de la paire de clés générée
openssl rsa -pubout -in private_key_generated.pem -out public_key_generated.pem


# Création d'un fichier texte à chiffrer
echo "Ceci est un message secret à chiffrer." > message.txt

# Chiffrer le message avec la clé publique
openssl rsautl -encrypt -inkey public_key_generated.pem -pubin -in message.txt -out message_encrypted.bin

# Chiffrer la passphrase avec la clé publique
echo "MaPassphraseSecrète" > passphrase.txt
openssl rsautl -encrypt -inkey public_key_generated.pem -pubin -in passphrase.txt -out passphrase_encrypted.bin

# Déchiffrer le message avec la clé privée
openssl rsautl -decrypt -inkey private_key_generated.pem -in message_encrypted.bin  
