FROM ubuntu:22.04

#MAJ des paquets
RUN apt-get update && apt-get upgrade -y

#installation de paquets
RUN apt-get install python3 nano htop git -y

#Définition des variables d'environnement
ENV TERM xterm-color


CMD ["bash"]