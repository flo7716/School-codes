# Importation des bibliothèques nécessaires
import numpy as np
from scipy.linalg import lstsq
from PIL import Image, ImageOps
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from sklearn.model_selection import train_test_split
import os

# Étape 1 : Prétraitement des images

def preprocess_image(image_path, output_size=(64, 64)):
    """
    Charge et normalise une image :
    - Convertit en niveaux de gris
    - Recadre pour enlever les marges blanches
    - Redimensionne à la taille spécifiée
    
    :param image_path: Chemin vers l'image
    :param output_size: Taille de sortie (largeur, hauteur)
    :return: Tableau numpy de l'image prétraitée
    """
    image = Image.open(image_path).convert("L")
    image = ImageOps.invert(image)  # Inverser pour mettre le fond en blanc et le texte en noir
    bbox = image.getbbox()
    image = image.crop(bbox) if bbox else image
    image = image.resize(output_size, Image.ANTIALIAS)
    return np.array(image)

# Étape 2 : Extraction des caractéristiques avec LLF

def extract_features(image_array, grid_size=(5, 5)):
    """
    Extrait des caractéristiques d'une image en utilisant la méthode LLF (Local Line Fitting).
    
    :param image_array: Tableau numpy de l'image en niveaux de gris
    :param grid_size: Taille de la grille pour diviser l'image
    :return: Vecteur des caractéristiques
    """
    h, w = image_array.shape
    cell_h, cell_w = h // grid_size[0], w // grid_size[1]
    features = []

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            cell = image_array[i * cell_h:(i + 1) * cell_h, j * cell_w:(j + 1) * cell_w]
            black_pixels = np.sum(cell < 128)  # Les pixels noirs
            density = black_pixels / (cell_h * cell_w)

            y, x = np.where(cell < 128)
            if len(x) > 1:
                A = np.vstack([x, np.ones_like(x)]).T
                slope, _ = lstsq(A, y)[0]
                f2 = (2 * slope) / (1 + slope**2)
                f3 = (1 - slope**2) / (1 + slope**2)
            else:
                f2, f3 = 0, 0

            features.extend([density, f2, f3])

    return np.array(features)

# Étape 3 : Préparation des données

def prepare_dataset(image_dir, grid_size=(5, 5)):
    """
    Charge et traite toutes les images d'un répertoire pour créer un dataset.

    :param image_dir: Répertoire contenant les images
    :param grid_size: Taille de la grille pour LLF
    :return: X (caractéristiques), y (étiquettes)
    """
    X, y = [], []
    labels = {"b": 0, "h": 1, "k": 2, "g": 3, "j": 4, "f": 5}

    for label, class_id in labels.items():
        class_dir = os.path.join(image_dir, label)
        for file in os.listdir(class_dir):
            image_path = os.path.join(class_dir, file)
            image_array = preprocess_image(image_path)
            features = extract_features(image_array, grid_size=grid_size)
            X.append(features)
            y.append(class_id)

    return np.array(X), np.array(y)

# Étape 4 : Construction et Entraînement du modèle

def build_model(input_dim, output_dim):
    """
    Crée un modèle de réseau de neurones pour la classification des caractères.

    :param input_dim: Dimension des vecteurs d'entrée
    :param output_dim: Nombre de classes (sorties)
    :return: Modèle Keras compilé
    """
    model = Sequential([
        Dense(128, activation="relu", input_dim=input_dim),
        Dense(64, activation="relu"),
        Dense(output_dim, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

# Étape 5 : Évaluation et Prédiction

def main():
    # Préparer les données
    image_dir = "dataset/"  # Chemin vers le dataset organisé par classe
    X, y = prepare_dataset(image_dir)

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Construire le modèle
    input_dim = X.shape[1]
    output_dim = len(set(y))
    model = build_model(input_dim, output_dim)

    # Entraîner le modèle
    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

    # Évaluer le modèle
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Précision sur le test : {accuracy * 100:.2f}%")

    # Sauvegarder le modèle
    model.save("handwriting_recognition_model.h5")

if __name__ == "__main__":
    main()
