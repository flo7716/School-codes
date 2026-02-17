#!/bin/bash

# Vérification installation d'OpenSSL
openssl version -a

# RSA avec openSSL
openssl genrsa -out private.pem 2048

# Visualisation des clés RSA
openssl rsa -in private.pem -text -noout


