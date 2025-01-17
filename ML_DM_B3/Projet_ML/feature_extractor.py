import os
import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import customtkinter as ctk
from PIL import ImageGrab
import pickle

# Paramètres globaux
num_squares = 8
square_size = 64
output_file = 'coefficients_letters.csv'

# Fonction de transformation des coefficients
def transform_coefficients(a):
    if a == 0:
        return 0, 1
    fi2 = (2 * a) / (1 + a**2)
    fi3 = (1 - a**2) / (1 + a**2)
    return fi2, fi3

# Conversion lettre -> binaire
def letter_to_binary(label):
    binary_mapping = {
        'b': '000',
        'f': '001',
        'g': '010',
        'h': '011',
        'j': '100',
        'k': '101',
    }
    return binary_mapping.get(label, '000')

# Conversion binaire -> lettre

def binary_to_letter(binary):
    # Conversion explicite du binaire en chaîne (par sécurité)
    binary = str(binary).strip()

    # Vérification des clés et recherche dans le dictionnaire
    letter_mapping = {
        '000': 'b',
        '001': 'f',
        '010': 'g',
        '011': 'h',
        '100': 'j',
        '101': 'k',
    }

    # Debugging : Afficher la valeur du binaire reçu
    print(f"Binary reçu pour conversion : '{binary}'")

    # Rechercher dans le dictionnaire
    return letter_mapping.get(binary, 'Inconnu')


# Générer le fichier CSV avec les coefficients transformés
def generate_coefficients_csv(dataset_path):
    with open(output_file, 'w') as file:
        # Génération de l'en-tête CSV
        header = [f"fi2_{i},fi3_{i}" for i in range((square_size // num_squares) ** 2)]  # Basé sur num_squares = 8
        file.write(",".join(header) + ",label\n")

        for lettre in os.listdir(dataset_path):
            folder_path = os.path.join(dataset_path, lettre)
            if not os.path.isdir(folder_path):
                continue

            for filename in os.listdir(folder_path):
                image_path = os.path.join(folder_path, filename)
                if image_path.endswith(('.png', '.jpg', '.jpeg')):
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    if image is None:
                        print(f"Impossible de charger l'image {image_path}.")
                        continue

                    list_features = []
                    for i in range(num_squares):  # 8 sous-divisions (num_squares)
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

                                fi2, fi3 = transform_coefficients(a)
                                list_features += [fi2, fi3]
                            else:
                                list_features += [0, 0]

                    binary_label = letter_to_binary(lettre)
                    line = ",".join(map(str, list_features)) + f",{binary_label}\n"
                    file.write(line)
    print(f"Fichier {output_file} généré.")

# Charger les données, entraîner et évaluer le modèle
def train_and_evaluate_model():
    data = pd.read_csv(output_file)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2021)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    param_grid = {
        'hidden_layer_sizes': [(64,), (64, 32), (128, 64, 32)], 
        'activation': ['relu', 'tanh'],  
        'solver': ['adam', 'sgd', 'lbfgs'],  
        'alpha': [0.0001, 0.001], 
        'learning_rate': ['constant', 'adaptive'],  
        'max_iter': [500, 1000, 1500] 
    }

    mlp = MLPClassifier(random_state=2021)

    grid_search = GridSearchCV(mlp, param_grid, cv=5, scoring='f1_macro', n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)

    print(f"Meilleurs paramètres : {grid_search.best_params_}")

    best_model = grid_search.best_estimator_

    y_pred = best_model.predict(X_test)
    print("\nRapport de classification :\n", classification_report(y_test, y_pred, target_names=[f"Classe {i}" for i in range(6)]))

    with open("best_model.pkl", "wb") as file:
        pickle.dump(best_model, file)
    print("Modèle sauvegardé dans 'best_model.pkl'.")

# Phase de reconnaissance avec une image utilisateur
def recognize_user_image(model):
    save_canvas()
    x, y, x1, y1 = canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + canvas.winfo_width(), canvas.winfo_rooty() + canvas.winfo_height()

    # Capturer l'image du canvas
    image = ImageGrab.grab(bbox=(x, y, x1, y1)).convert('L')
    user_image = np.array(image)

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
    canvas.delete("all")
    messagebox.showinfo("Résultat", f"La lettre prédite est : {predicted_letter}")


# Exécuter les étapes
generate_coefficients_csv()
model = train_and_evaluate_model()
recognize_user_image(model)


# -----------------------Interface graphique-----------------------
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    if last_x and last_y:
        canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=10)
        last_x, last_y = event.x, event.y

def reset(event=None):
    global last_x, last_y
    last_x, last_y = None, None

def save_canvas():
    x, y, x1, y1 = canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + canvas.winfo_width(), canvas.winfo_rooty() + canvas.winfo_height()
    image = ImageGrab.grab(bbox=(x, y, x1, y1))
    
    image = image.convert("RGB")
    
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if filepath:
        image.save(filepath, "PNG")

root = ctk.CTk()
root.title("Application de Dessin")
root.geometry("400x400")
root.config(bg="black")

frame = ctk.CTkFrame(root, width=380, height=50, corner_radius=10)
frame.pack(padx=5, pady=10)

frame2 = ctk.CTkFrame(root, width=380, height=8, corner_radius=10)
frame2.pack(padx=5, pady=5)

frame3 = ctk.CTkFrame(root, width=380, height=100, corner_radius=10)
frame3.pack(padx=10, pady=5)

frame4 = ctk.CTkFrame(root, width=380, height=50, corner_radius=10)
frame4.pack(padx=10, pady=5)

label1 = ctk.CTkLabel(frame, width=50, corner_radius=10, text="Application de Dessin", font=("ITC Avant Garde Gothic LT Bold", 16))
label1.pack(padx=5, pady=5)

label2 = ctk.CTkLabel(frame2, width=50, corner_radius=10, text="Dessinez ici :", font=("ITC Avant Garde Gothic LT Bold", 14))
label2.pack(padx=5, pady=5)

canvas = tk.Canvas(frame3, bg="white", width=508, height=508)
canvas.pack(padx=5, pady=5)

boutton_delete = ctk.CTkButton(frame4, width=50, corner_radius=10, text="Effacer", font=("ITC Avant Garde Gothic LT Bold", 14), command=lambda: canvas.delete("all"))
boutton_delete.grid(row=0, column=1, padx=5, pady=5)

boutton_save = ctk.CTkButton(frame4, width=50, corner_radius=10, text="Reconnaître", font=("ITC Avant Garde Gothic LT Bold", 14), command=lambda: recognize_user_image(model))
boutton_save.grid(row=0, column=2, padx=5, pady=5)

boutton_quit = ctk.CTkButton(frame4, width=50, corner_radius=10, fg_color="red", hover_color="darkred", text_color="white", text="Quitter", font=("ITC Avant Garde Gothic LT Bold", 14), command=root.quit)
boutton_quit.grid(row=0, column=0, padx=5, pady=5)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset)

root.mainloop()