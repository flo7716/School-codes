#!/bin/bash

# --------------------------------------------
# Script installation Docker sur Fedora
# --------------------------------------------

# Met à jour le système
sudo dnf -y update

# Installe les dépendances nécessaires
sudo dnf -y install dnf-plugins-core curl

# Ajoute le dépôt officiel Docker
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

# Installe Docker Engine, CLI, containerd, Buildx et Compose
sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Active et démarre le service Docker
sudo systemctl enable --now docker

# Ajoute l’utilisateur courant au groupe "docker" (pour éviter sudo à chaque fois)
sudo usermod -aG docker $USER

# Vérifie que Docker tourne correctement
sudo systemctl status docker --no-pager

# Test avec l’image hello-world
docker run hello-world

echo "✅ Installation Docker terminée sur Fedora !"
echo "ℹ️ Déconnecte-toi / reconnecte-toi pour que ton utilisateur soit bien ajouté au groupe docker."
