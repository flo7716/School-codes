FROM fedora:latest

# Mise à jour des paquets

RUN dnf update -y

# Installation de paquets
RUN dnf install -y python3 iproute iputils nano htop net-tools curl wget git

# Installation d'Ansible
RUN dnf install -y ansible ansible-playbook ansible-galaxy

# Clonage du dépôt IPSA_TP_Linux_Docker
RUN git clone https://github.com/flo7716/School-codes



# Définition de variables d'environnement
ENV TERM=xterm-color

CMD ["bash"]

