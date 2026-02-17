#!/bin/bash

# Vérification installation d'OpenSSL
openssl version -a

# RSA avec openSSL
openssl genrsa -out private.pem 2048

# Visualisation des clés RSA
openssl rsa -in private.pem -text -noout


# Chiffrement d'un fichier de clés RSA (DES, DES3 ou IDEA)
openssl rsa -in private.pem -des3 -out private_des3.pem
openssl rsa -in private.pem -des -out private_des.pem
openssl rsa -in private.pem -idea -out private_idea.pem

# Visualisation des clés RSA chiffrées
cat private_des3.pem
cat private_des.pem
cat private_idea.pem


