import os
import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
import pandas as pd

# Paramètres
if os.name == 'nt':
    directory_path = 'mets ton chemin ici Hector !'
else:
    directory_path = '/home/florian-andr/Downloads/dataset(2)/dataset'

lettres = ['b', 'f', 'g', 'h', 'j', 'k']  # Lettres à analyser
square_size = 64
num_squares = 8
output_file = 'coefficients_letters.csv'

# Fonction pour obtenir le code binaire correspondant à chaque lettre
def letter_to_binary(label):
    binary_mapping = {
        'b': '000',
        'f': '001',
        'g': '010',
        'h': '011',
        'j': '100',
        'k': '101',
    }
    return binary_mapping.get(label, '000')  # Valeur par défaut '000' pour éviter toute erreur

# Inverser la correspondance binaire -> lettre
binary_to_letter = {
    '000': 'b',
    '001': 'f',
    '010': 'g',
    '011': 'h',
    '100': 'j',
    '101': 'k'
}

# Générer le fichier CSV avec les coefficients et les labels binaires
def generate_coefficients_csv():
    with open(output_file, 'w') as file:
        # En-tête du fichier CSV
        file.write(",".join([f"a{i},fi2_{i},fi3_{i}" for i in range(num_squares**2)]) + ",label\n")

        for lettre in lettres:
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

                    list_features = []
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
                                a = model.coef_[0]

                                # Calcul des nouveaux paramètres fi2 et fi3
                                fi2 = (2 * a) / (1 + a**2)
                                fi3 = (1 - a**2) / (1 + a**2)

                                list_features += [a, fi2, fi3]
                            else:
                                list_features += [0, 0, 0]

                    # Utiliser le code binaire pour la lettre
                    binary_label = letter_to_binary(lettre)
                    line = ",".join(map(str, list_features)) + f",{binary_label}\n"
                    file.write(line)
    print(f"Fichier {output_file} généré.")


# Charger les données du CSV et entraîner le modèle avec GridSearchCV
def train_model_with_gridsearch():
    data = pd.read_csv(output_file)
    X = data.iloc[:, :-1].values  # Features (les coefficients)
    y = data.iloc[:, -1].values  # Labels binaires

    # Diviser en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Définir les hyperparamètres à tester dans GridSearch
    param_grid = {
        'hidden_layer_sizes': [(128, 64), (256, 128), (512, 256)],
        'activation': ['relu', 'tanh'],
        'solver': ['adam', 'sgd'],
        'learning_rate': ['constant', 'adaptive'],
        'max_iter': [200, 300],
        'batch_size': [64]
    }

    # Initialiser le classificateur MLP sans l'entraîner
    mlp = MLPClassifier(random_state=42)

    # GridSearch pour trouver les meilleurs paramètres
    grid_search = GridSearchCV(mlp, param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)

    # Résultats du GridSearch
    print("Meilleurs paramètres trouvés :", grid_search.best_params_)
    best_model = grid_search.best_estimator_

    # Évaluation du modèle sur l'ensemble de test
    y_pred = best_model.predict(X_test)
    print("Rapport de classification :\n", classification_report(y_test, y_pred))

    return best_model

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
    predicted_binary = model.predict(user_coefficients)[0]

    # Convertir la valeur binaire en lettre
    predicted_letter = binary_to_letter.get(predicted_binary, 'Inconnu')
    print(f"La lettre prédite est : {predicted_letter}")

# Exécuter les étapes
generate_coefficients_csv()
model = train_model_with_gridsearch()

# Demander une image utilisateur
user_image_path = input("Entrez le chemin de l'image PNG à reconnaître : ")
recognize_user_image(user_image_path, model)
