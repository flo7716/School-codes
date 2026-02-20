#Dockerfile qui installe les dépendances pour l'image ubuntu et crée un environnement pour l'examen de cryptologie (avec user Florian)
FROM ubuntu:latest
# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-pip \
    vim \  
    && rm -rf /var/lib/apt/lists/*

# Create a user named Florian
RUN useradd -m -s /bin/bash florian 
# Set the working directory
WORKDIR /home/florian
# Install Python dependencies (if any)
# For example, if you have a requirements.txt file, you can copy it and install the dependencies
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt  


# Installation des dépendances pour l'examen de cryptologie (contenues dans les TP de ce repo)
RUN apt-get update && apt-get install -y \
    openssl \
    gpg \
    && rm -rf /var/lib/apt/lists/*

# Set the default command to bash
CMD ["/bin/bash"]