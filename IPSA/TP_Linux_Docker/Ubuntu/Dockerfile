FROM ubuntu:24.04

# Mise à jour des paquets
RUN apt update && apt upgrade -y

# Installation de paquets
RUN apt-get update && apt-get upgrade -y
RUN apt install -y python3 iproute2 iputils-ping nano htop net-tools curl wget git

# Définition de variables d'environnement
ENV TERM xterm-color

CMD ["bash"]
