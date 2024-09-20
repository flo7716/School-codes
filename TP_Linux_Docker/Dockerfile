FROM ubuntu:20.04

# Mise à jour des paquets
RUN apt update && apt upgrade -y

# Installation de paquets
RUN apt-get update && apt-get upgrade -y
RUN apt install -y python3 iproute2 iputils-ping

# Définition de variables d'environnement
ENV TERM xterm-color

CMD ["bash"]
