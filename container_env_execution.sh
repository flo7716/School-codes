#!/bin/bash

# Nom du conteneur et de l'image
CONTAINER_NAME="contenv"
IMAGE_NAME="my-python-app"
GITHUB_REPO="https://github.com/flo7716/School-codes"

# Vérifier si le conteneur existe
if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
    echo "Le conteneur '$CONTAINER_NAME' existe déjà. Démarrage du conteneur..."
    docker start $CONTAINER_NAME
    echo "Attachement au conteneur..."
    docker attach $CONTAINER_NAME
else
    echo "Le conteneur '$CONTAINER_NAME' n'existe pas. Création de l'image et du conteneur..."
    
    # Créer l'image Docker à partir du Dockerfile
    docker build -t $IMAGE_NAME .

    # Exécuter le conteneur
    docker run -it --name $CONTAINER_NAME -v $(pwd):/app -p 8080:8080 $IMAGE_NAME

    # Cloner le dépôt git dans /Documents/School-codes
    cd Documents && mkdir School-codes
    cd School-codes
    git clone $GITHUB_REPO
fi
