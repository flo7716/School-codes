import cv2
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import os

# Fichier CSV contenant les coefficients
csv_path = 'coefficients_letters.csv'

# Charger les données du CSV
data = pd.read_csv(csv_path)

# Séparer les caractéristiques (X) et les labels (y)
X = data.iloc[:, :-1].values  # Toutes les colonnes sauf la dernière
y = data.iloc[:, -1].values  # La dernière colonne (lettres)

# Diviser les données en ensemble d'apprentissage et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un réseau de neurones multi-couches
model = MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', max_iter=500, random_state=42)

# Phase d'apprentissage
model.fit(X_train, y_train)
print("Apprentissage terminé.")

# Phase de test
y_pred = model.predict(X_test)
print("Rapport de classification :\n", classification_report(y_test, y_pred))

# Phase de reconnaissance avec une image utilisateur
def process_user_image(image_path, model):
    # Charger l'image utilisateur (convertir en niveaux de gris)
    user_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if user_image is None:
        print(f"Erreur : Impossible de charger l'image {image_path}")
        return

    # Paramètres des carrés
    square_size = 64
    num_squares = 8

    # Initialiser la liste des coefficients pour cette image
    user_coefficients = []

    # Parcourir l'image en carrés 8x8
    for i in range(num_squares):
        for j in range(num_squares):
            # Extraire un carré de taille 64x64
            x_start = i * square_size
            y_start = j * square_size
            square = user_image[y_start:y_start + square_size, x_start:x_start + square_size]

            # Trouver les pixels noirs (valeur 0 dans l'image en niveaux de gris)
            black_pixels = []
            for y in range(square_size):
                for x in range(square_size):
                    if square[y, x] == 0:  # Pixel noir
                        black_pixels.append((x, y))

            if len(black_pixels) > 0:
                # Convertir les coordonnées en arrays pour la régression
                X_pixels = np.array([x for x, y in black_pixels]).reshape(-1, 1)
                y_pixels = np.array([y for x, y in black_pixels])

                # Appliquer la régression linéaire
                from sklearn.linear_model import LinearRegression
                model_lr = LinearRegression()
                model_lr.fit(X_pixels, y_pixels)

                a, b = model_lr.coef_[0], model_lr.intercept_
                user_coefficients += [a, b]
            else:
                # Si aucun pixel noir n'est trouvé, ajouter des coefficients nuls
                user_coefficients += [0, 0]

    # Vérifier que le nombre de coefficients correspond à l'entraînement
    if len(user_coefficients) != X_train.shape[1]:
        print(f"Erreur : le nombre de coefficients ({len(user_coefficients)}) ne correspond pas à celui attendu ({X_train.shape[1]}).")
        return

    # Convertir les coefficients en array et prédire la lettre
    user_coefficients = np.array(user_coefficients).reshape(1, -1)
    predicted_letter = model.predict(user_coefficients)[0]
    print(f"La lettre prédite est : {predicted_letter}")

# Demander à l'utilisateur d'entrer le chemin d'une image pour reconnaissance
user_image_path = input("Entrez le chemin de l'image PNG à reconnaître : ")
process_user_image(user_image_path, model)
