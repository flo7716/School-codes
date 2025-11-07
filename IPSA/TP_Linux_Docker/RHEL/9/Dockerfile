FROM registry.access.redhat.com/ubi9/ubi:latest

#ajout user non-root
RUN useradd -m -u 1001 appuser

#définition du répertoire de travail
WORKDIR /home/appuser
USER appuser

#copie de l'application
COPY app/ /home/appuser/app

#configuration des droits
RUN chown -R appuser:appuser /home/appuser

#passage en mode non-root
USER 1001

#exposition du port
EXPOSE 8080

#commande de démarrage de l'application
# Définition de variables d'environnement
ENV TERM=xterm-color
CMD ["bash"]