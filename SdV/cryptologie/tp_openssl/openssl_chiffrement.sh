#!/bin/bash

# Chiffrement d'un fichier de clés RSA (DES, DES3 ou IDEA)
openssl rsa -in private.pem -des3 -out private_des3.pem

# Visualisation des clés RSA chiffrées
cat private_des3.pem