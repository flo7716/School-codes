#!/bin/bash

# Création d'un fichier texte à signer
echo "Ceci est un message à signer." > message_to_sign.txt

# signer le message avec la clé privée
openssl pkeyutl -sign -inkey private_key_generated.pem -in message_to_sign.txt -out signature.bin

# Vérifier la signature avec la clé publique
openssl pkeyutl -verify -pubin -inkey public_key_generated.pem -in message_to_sign.txt -sigfile signature.bin
