import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Charger l'image (convertir en niveau de gris)
image = cv2.imread('/home/florian-andr/Downloads/lettre/f/f (10).png', cv2.IMREAD_GRAYSCALE)

# Taille des carrés
square_size = 64

# Nombre de carrés
num_squares = 8

# Créer une copie de l'image pour afficher les régressions et les carrés
image_with_regressions = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

list_a_b = []
# Parcourir l'image en carrés 8x8
for i in range(num_squares):
    for j in range(num_squares):
        # Extraire un carré de taille 64x64
        x_start = i * square_size
        y_start = j * square_size
        square = image[y_start:y_start + square_size, x_start:x_start + square_size]

        # Trouver les pixels noirs (valeur 0 dans l'image en niveaux de gris)
        black_pixels = []
        for x in range(square_size):
            for y in range(square_size):
                if square[x, y] == 0:  # Pixel noir
                    # Ajouter les coordonnées x, y du pixel noir
                    black_pixels.append((x, y))

        if len(black_pixels) > 0:
            # Convertir les coordonnées x, y des pixels noirs en arrays pour la régression
            X = np.array([x for x, y in black_pixels]).reshape(-1, 1)  # Coordonnées x
            y = np.array([y for x, y in black_pixels]).reshape(-1, 1)  # Coordonnées y

            # Appliquer la régression linéaire pour prédire les j (valeurs de y)
            model = LinearRegression()
            model.fit(X, y)

            a,b = model.coef_[0][0], model.intercept_[0]
            list_a_b += [a,b]
            # Prédictions des j à partir des x
            y_pred = model.predict(X)

            # Afficher les prédictions sur l'image d'origine
            for idx, (x, y) in enumerate(black_pixels):
                # Replacer les points de régression sur l'image originale
                pred_y = int(y_pred[idx])
                if 0 <= x + x_start < image.shape[1] and 0 <= pred_y + y_start < image.shape[0]:
                    image_with_regressions[pred_y + y_start, x + x_start] = [0, 0, 255]  # Marquer en rouge
        else:
            list_a_b += [0,0]
        # Dessiner un rectangle autour de chaque carré 64x64 sur l'image
        cv2.rectangle(image_with_regressions, (x_start, y_start), (x_start + square_size, y_start + square_size), (0, 255, 0), 2)

print(list_a_b)
# Afficher l'image avec les régressions et les carrés
# Enregistrer la liste en tant que ligne dans un .txt
list_a_b = [str(x) for x in list_a_b]
with open('list_a_b.txt', 'w') as file:
        file.write(",".join(list_a_b))

plt.imshow(image_with_regressions)
plt.title("Régressions linéaires et carrés sur la lettre")
plt.axis('off')  # Cacher les axes pour mieux voir l'image
plt.show()
