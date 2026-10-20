#!/bin/bash

EXERCISE_DIR="./exercice5"

RSA_KEY="$EXERCISE_DIR/Key.pem"
RSA_PASS=$(echo c3VwZGV2aW5jaQo= | base64 -d | tr -d '\n')

ENC_PASS_FILE="$EXERCISE_DIR/motDePasse1"
DEC_PASS_FILE="$EXERCISE_DIR/motDePasse1_dechiffre"

INPUT_FILE="$EXERCISE_DIR/exo5.chiffre"
OUTPUT_FILE="$EXERCISE_DIR/exo5_dechiffre.txt"

echo "[1/2] Déchiffrement du mot de passe Blowfish avec RSA..."

openssl pkeyutl \
-decrypt \
-provider default -provider legacy \
-inkey "$RSA_KEY" \
-in "$ENC_PASS_FILE" \
-out "$DEC_PASS_FILE" \
-passin pass:"$RSA_PASS"

echo "[2/2] Déchiffrement Blowfish..."

BLOWFISH_PASS=$(tr -d '\n' < "$DEC_PASS_FILE")

openssl enc \
-provider default -provider legacy \
-d \
-bf-cbc \
-iv 0000000000000000 \
-in "$INPUT_FILE" \
-out "$OUTPUT_FILE" \
-pass pass:"$BLOWFISH_PASS"

echo "Déchiffrement terminé : $OUTPUT_FILE"
