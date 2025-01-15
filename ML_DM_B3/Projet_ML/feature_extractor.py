import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os
import csv

# Dossier contenant les sous-dossiers des lettres
dataset_path = '/home/florian-andr/Downloads/dataset'
output_csv_path = 'coefficients_letters.csv'

# Taille des carrés
square_size = 64

# Nombre de carrés (8x8)
num_squares = 8

# Ouvrir le fichier CSV pour écrire les données
with open(output_csv_path, mode='w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Écrire l'en-tête du fichier CSV
    headers = [f'a_{i}_{j}' for i in range(num_squares) for j in range(num_squares)] + \
              [f'b_{i}_{j}' for i in range(num_squares) for j in range(num_squares)] + ['letter']
    csv_writer.writerow(headers)

    # Parcourir chaque sous-dossier (chaque lettre)
    for letter_folder in os.listdir(dataset_path):
        letter_path = os.path.join(dataset_path, letter_folder)
        
        # Vérifier si c'est un dossier
        if os.path.isdir(letter_path):
            # Parcourir chaque image dans le sous-dossier
            for image_name in os.listdir(letter_path):
                image_path = os.path.join(letter_path, image_name)
                
                # Charger l'image (convertir en niveau de gris)
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                if image is None:
                    print(f"Erreur de chargement pour l'image : {image_path}")
                    continue

                # Initialiser la liste des coefficients pour cette image
                list_a_b = []

                # Créer une copie de l'image pour afficher les régressions et les carrés (facultatif)
                image_with_regressions = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

                # Parcourir l'image en carrés 8x8
                for i in range(num_squares):
                    for j in range(num_squares):
                        # Extraire un carré de taille 64x64
                        x_start = i * square_size
                        y_start = j * square_size
                        square = image[y_start:y_start + square_size, x_start:x_start + square_size]

                        # Trouver les pixels noirs (valeur 0 dans l'image en niveaux de gris)
                        black_pixels = []
                        for y in range(square_size):  # Parcours en (y, x) car OpenCV utilise cette convention
                            for x in range(square_size):
                                if square[y, x] == 0:  # Pixel noir
                                    # Ajouter les coordonnées x, y du pixel noir
                                    black_pixels.append((x, y))

                        if len(black_pixels) > 0:
                            # Convertir les coordonnées x, y des pixels noirs en arrays pour la régression
                            X = np.array([x for x, y in black_pixels]).reshape(-1, 1)  # Coordonnées x
                            y = np.array([y for x, y in black_pixels])  # Coordonnées y

                            # Appliquer la régression linéaire pour prédire les j (valeurs de y)
                            model = LinearRegression()
                            model.fit(X, y)

                            a, b = model.coef_[0], model.intercept_
                            list_a_b += [a, b]
                        else:
                            # Si aucun pixel noir n'est trouvé, ajouter des coefficients nuls
                            list_a_b += [0, 0]

                        # Dessiner un rectangle autour de chaque carré 64x64 sur l'image (facultatif)
                        cv2.rectangle(image_with_regressions, (x_start, y_start), 
                                      (x_start + square_size, y_start + square_size), 
                                      (0, 255, 0), 2)

                # Ajouter la lettre (nom du sous-dossier) à la fin de la ligne
                list_a_b.append(letter_folder)

                # Écrire les coefficients et la lettre dans le fichier CSV
                csv_writer.writerow(list_a_b)

                # Afficher ou enregistrer l'image avec régressions (facultatif)
                # cv2.imshow("Image with Regressions", image_with_regressions)
                # cv2.waitKey(0)

print(f"Les coefficients ont été enregistrés dans {output_csv_path}.")
