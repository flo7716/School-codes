#!/bin/bash

# Déchiffrement du message chiffré avec Blowfish (ici exo5.chiffre avec Key.pem et motDePasse1 dans le sous-dossier exercice5)

EXERCISE_DIR="./exercice5"
KEY_FILE="${EXERCISE_DIR}/Key.pem"
INPUT_FILE="${EXERCISE_DIR}/exo5.chiffre"
OUTPUT_FILE="${EXERCISE_DIR}/exo5_dechiffre.txt"

# Check if key file exists
if [[ ! -f "$KEY_FILE" ]]; then
  echo "Error: Key file not found at $KEY_FILE" >&2
  exit 1
fi

openssl enc -d -blowfish -provider default -provider legacy \
  -in "$INPUT_FILE" \
  -out "$OUTPUT_FILE" \
  -pass file:"$KEY_FILE"

