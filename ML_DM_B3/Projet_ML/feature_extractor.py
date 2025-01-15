import os
import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from PIL import Image

# Paramètres
directory_path = '/home/florian-andr/Downloads/dataset'
lettres = ['b', 'f', 'g', 'h', 'j', 'k']  # Lettres à analyser
square_size = 64
num_squares = 8

# Fichier de sortie
output_file = 'list_a_b.txt'

# Ouvrir le fichier en mode écriture
with open(output_file, 'w') as file:
    for label, lettre in enumerate(lettres):  # Assigner un label pour chaque lettre
        folder_path = os.path.join(directory_path, lettre)

        if not os.path.exists(folder_path):
            print(f"Le dossier {folder_path} n'existe pas.")
            continue

        # Itérer à travers les fichiers dans le dossier de la lettre
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)

            if image_path.endswith(('.png', '.jpg', '.jpeg')):  # Filtrer les extensions d'image
                # Charger l'image en niveaux de gris
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

                if image is None:
                    print(f"Impossible de charger l'image {image_path}.")
                    continue

                # Créer une copie de l'image pour affichage des régressions
                image_with_regressions = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
                list_a_b = []

                # Parcourir l'image en carrés
                for i in range(num_squares):
                    for j in range(num_squares):
                        x_start = i * square_size
                        y_start = j * square_size
                        square = image[y_start:y_start + square_size, x_start:x_start + square_size]

                        # Trouver les pixels noirs
                        black_pixels = []
                        for y in range(square_size):  # Parcours en (y, x)
                            for x in range(square_size):
                                if square[y, x] == 0:  # Pixel noir
                                    black_pixels.append((x, y))

                        if len(black_pixels) > 0:
                            # Régression linéaire
                            X = np.array([x for x, y in black_pixels]).reshape(-1, 1)
                            y = np.array([y for x, y in black_pixels])
                            model = LinearRegression()
                            model.fit(X, y)

                            a, b = model.coef_[0], model.intercept_
                            list_a_b += [a, b]

                            # Prédictions des j à partir des x
                            y_pred = model.predict(X)

                            # Dessiner les prédictions sur l'image d'origine
                            for idx, x in enumerate(X.flatten()):
                                pred_y = int(y_pred[idx])
                                global_x = x + x_start
                                global_y = pred_y + y_start

                                if 0 <= global_x < image_with_regressions.shape[1] and 0 <= global_y < image_with_regressions.shape[0]:
                                    image_with_regressions[global_y, global_x] = [0, 0, 255]  # Rouge
                        else:
                            list_a_b += [0, 0]

                        # Dessiner un rectangle autour de chaque carré
                        cv2.rectangle(image_with_regressions, (x_start, y_start), (x_start + square_size, y_start + square_size), (0, 255, 0), 2)

                # Sauvegarder la liste a, b avec la lettre
                list_a_b = [str(x) for x in list_a_b]
                line = ",".join(list_a_b) + f",{lettre}\n"
                file.write(line)

                # Afficher une image de régression pour vérification
                plt.imshow(cv2.cvtColor(image_with_regressions, cv2.COLOR_BGR2RGB))
                plt.title(f"Régressions et carrés pour {lettre} ({filename})")
                plt.axis('off')
                plt.show()

print(f"Traitement terminé. Les coefficients sont sauvegardés dans {output_file}.")
