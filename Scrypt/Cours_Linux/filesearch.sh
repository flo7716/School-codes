#!/bin/bash

WORKDIR="/Scrypt/Cours_Linux"


for file in $(ls $WORKDIR); do
    if [ -d "$WORKDIR/$file" ]; then
        echo "$file est un répertoire"
    else
        echo "$file est un fichier"
        cat $WORKDIR/$file
    fi
done