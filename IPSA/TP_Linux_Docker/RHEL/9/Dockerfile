FROM registry.access.redhat.com/ubi9/ubi:latest

#ajout user non-root
RUN useradd -m -u 1001 appuser

#définition du répertoire de travail
WORKDIR /home/appuser
USER appuser


#configuration des droits
RUN chown -R appuser:appuser /home/appuser

#passage en mode non-root
USER 1001

#exposition du port
EXPOSE 8080

#installation des paquets nécessaires
RUN sudo dnf update -y && sudo dnf install -y python3 iproute iputils nano htop net-tools curl wget git

#commande de démarrage de l'application
# Définition de variables d'environnement
ENV TERM=xterm-color
CMD ["bash"]