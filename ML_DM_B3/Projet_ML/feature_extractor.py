import os
import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import pandas as pd

# Paramètres
directory_path = '/home/florian-andr/Downloads/dataset'
lettres = ['b', 'f', 'g', 'h', 'j', 'k']  # Lettres à analyser
square_size = 64
num_squares = 8
output_file = 'coefficients_letters.csv'

# Générer le fichier CSV avec les coefficients
def generate_coefficients_csv():
    with open(output_file, 'w') as file:
        file.write(",".join([f"a{i},b{i}" for i in range(num_squares**2)]) + ",label\n")

        for label, lettre in enumerate(lettres):
            folder_path = os.path.join(directory_path, lettre)
            if not os.path.exists(folder_path):
                print(f"Le dossier {folder_path} n'existe pas.")
                continue

            for filename in os.listdir(folder_path):
                image_path = os.path.join(folder_path, filename)
                if image_path.endswith(('.png', '.jpg', '.jpeg')):
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    if image is None:
                        print(f"Impossible de charger l'image {image_path}.")
                        continue

                    list_a_b = []
                    for i in range(num_squares):
                        for j in range(num_squares):
                            x_start = i * square_size
                            y_start = j * square_size
                            square = image[y_start:y_start + square_size, x_start:x_start + square_size]

                            black_pixels = [(x, y) for y in range(square_size) for x in range(square_size) if square[y, x] == 0]
                            if black_pixels:
                                X = np.array([x for x, y in black_pixels]).reshape(-1, 1)
                                y = np.array([y for x, y in black_pixels])
                                model = LinearRegression()
                                model.fit(X, y)
                                a, b = model.coef_[0], model.intercept_
                                list_a_b += [a, b]
                            else:
                                list_a_b += [0, 0]

                    line = ",".join(map(str, list_a_b)) + f",{lettre}\n"
                    file.write(line)
    print(f"Fichier {output_file} généré.")

# Charger les données du CSV et entraîner le modèle
def train_model():
    data = pd.read_csv(output_file)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', max_iter=500, random_state=42)
    model.fit(X_train, y_train)
    print("Apprentissage terminé.")
    y_pred = model.predict(X_test)
    print("Rapport de classification :\n", classification_report(y_test, y_pred))
    return model

# Phase de reconnaissance avec une image utilisateur
def recognize_user_image(image_path, model):
    user_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if user_image is None:
        print(f"Erreur : Impossible de charger l'image {image_path}")
        return

    user_coefficients = []
    for i in range(num_squares):
        for j in range(num_squares):
            x_start = i * square_size
            y_start = j * square_size
            square = user_image[y_start:y_start + square_size, x_start:x_start + square_size]

            black_pixels = [(x, y) for y in range(square_size) for x in range(square_size) if square[y, x] == 0]
            if black_pixels:
                X = np.array([x for x, y in black_pixels]).reshape(-1, 1)
                y = np.array([y for x, y in black_pixels])
                model_lr = LinearRegression()
                model_lr.fit(X, y)
                a, b = model_lr.coef_[0], model_lr.intercept_
                user_coefficients += [a, b]
            else:
                user_coefficients += [0, 0]

    if len(user_coefficients) != len(model.coefs_[0]):
        print(f"Erreur : le nombre de coefficients ({len(user_coefficients)}) ne correspond pas à celui attendu.")
        return

    user_coefficients = np.array(user_coefficients).reshape(1, -1)
    predicted_letter = model.predict(user_coefficients)[0]
    print(f"La lettre prédite est : {predicted_letter}")

# Exécuter les étapes
generate_coefficients_csv()
model = train_model()

# Demander une image utilisateur
user_image_path = input("Entrez le chemin de l'image PNG à reconnaître : ")
recognize_user_image(user_image_path, model)
