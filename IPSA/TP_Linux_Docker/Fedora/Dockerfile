FROM fedora:latest

# Mise à jour des paquets

RUN dnf update -y

# Installation de paquets
RUN dnf install -y python3 iproute iputils nano htop net-tools curl wget git

# Définition de variables d'environnement
ENV TERM=xterm-color

CMD ["bash"]

