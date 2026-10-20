#!/bin/bash

# Générer un certificat pour notre AC
openssl req -new -x509 -key private_key_generated.pem -out certificate_generated.pem -days 365 -subj "/CN=My CA/O=My Organization/C=US"

# Afficher le certificat généré
openssl x509 -in certificate_generated.pem -text -noout

# Autosigner un certificat pour notre AC
openssl req -new -key private_key_generated.pem -out certificate_request.pem -subj "/CN=My CA/O=My Organization/C=US"
openssl x509 -req -in certificate_request.pem -signkey private_key_generated.pem -out certificate_self_signed.pem -days 365

# Afficher le certificat autosigné
openssl x509 -in certificate_self_signed.pem -text -noout

# Générer une demande de certificat pour une entité "test"
openssl req -new -key private_key_generated.pem -out certificate_request_test.pem -subj "/CN=Test Entity/O=Test Organization/C=US"

# Signer la demande de certificat avec notre AC
openssl x509 -req -in certificate_request_test.pem -CA certificate_generated.pem -CAkey private_key_generated.pem -CAcreateserial -out certificate_signed_by_ca.pem -days 365

# Vérifier le certificat signé par l'AC pour l'entité "test"
openssl verify -CAfile certificate_generated.pem certificate_signed_by_ca.pem
