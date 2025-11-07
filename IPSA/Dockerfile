# Utilise une image Python officielle avec une version spécifique
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de votre projet dans le conteneur
COPY . /app

# Installer les dépendances système requises pour certaines bibliothèques (si nécessaire)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installer les bibliothèques Python
RUN pip install --no-cache-dir scikit-learn beautifulsoup4 nltk requests flask ipykernel seaborn matplotlib pandas statsmodels

