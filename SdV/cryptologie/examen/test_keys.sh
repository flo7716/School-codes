#!/bin/bash

DOSSIER="./fichier-examen/exercice3"
> resultat.txt

# Liste des documents et des clés
DOCUMENTS=$(ls "$DOSSIER" | grep "^document")
CLES=$(ls "$DOSSIER" | grep "^cle")

# Boucle sur tous les documents
for document in $DOCUMENTS; do
    doc_path="$DOSSIER/$document"
    num=$(echo "$document" | grep -o '[0-9]\+')
    signature="$DOSSIER/signature-document${num}"
    hash_file="$DOSSIER/hashdoc${num}.bin"

    # Vérifier que la signature existe
    if [ ! -f "$signature" ]; then
        echo "Signature non trouvée pour $document" >> resultat.txt
        continue
    fi

    # Calcul du hash MD5 binaire du document
    openssl dgst -md5 -binary -out "$hash_file" "$doc_path"

    # Boucle sur toutes les clés
    for cle in $CLES; do
        cle_path="$DOSSIER/$cle"
        openssl pkeyutl -verify -in "$hash_file" -inkey "$cle_path" -sigfile "$signature"
        if [ $? -eq 0 ]; then
            echo "Document $document signé par $cle" >> resultat.txt
        fi
    done

    # Supprimer le fichier hash temporaire
    rm -f "$hash_file"
done
