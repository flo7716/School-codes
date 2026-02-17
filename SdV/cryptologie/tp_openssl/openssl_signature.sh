#!/bin/bash

# Création d'un fichier texte à signer
echo "Ceci est un message à signer." > message_to_sign.txt

# signer le message avec la clé privée
openssl dgst -sha256 -sign private_key_generated.pem -out signature.bin message_to_sign.txt

# Vérifier la signature avec la clé publique
openssl dgst -sha256 -verify public_key_generated.pem -signature signature.bin message_to_sign.txt
