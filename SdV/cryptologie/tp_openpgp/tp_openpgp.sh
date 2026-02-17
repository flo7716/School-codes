#!/bin/bash

#Lancer la génération de la paire de clés GPG

gpg --full-generate-key

#Lister les clés générées et leurs ID
gpg --list-secret-keys --keyid-format 0xlong

#Exporter la clé publique dans un fichier pour la copier dans une autre machine qui devra vérifier la signature du fichier
gpg --armor --export "testkey<test@key.local>"> public_key_gpg.asc

#Importer la clé publique contenue dans le fichier asc
gpg --import public_key_gpg.asc

#Signer un binaire avec la clé privée
echo "Ceci est un message à signer." > message_to_sign.txt
gpg --armor --output signature_gpg.asc --detach-sig message_to_sign.txt

#Vérifier la signature du fichier avec la clé publique
gpg --verify signature_gpg.asc message_to_sign.txt



