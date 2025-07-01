import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import time
import matplotlib.pyplot as plt
import random
import pandas as pd
import os, csv
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
import pickle
from PIL import Image
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def transform_coefficients(a):
    if a == 0:
        return 0, 1
    a_prime = (2 * a) / (1 + a**2)
    b_prime = (1 - a**2) / (1 + a**2)
    return a_prime, b_prime

def split_and_process_image(image, save_dir, csv_filename, image_name, extra_variable, square_size=64):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    row_data = [image_name]
    width, height = image.size
    regression_results = []

    for j in range(0, height, square_size):
        for i in range(0, width, square_size):
            box = (i, j, i + square_size, j + square_size)
            square = image.crop(box)

            square_array = np.array(square.convert("L"))
            mask = square_array < 128
            y_coords, x_coords = np.where(mask)

            if len(x_coords) > 10:
                x_data = x_coords.reshape(-1, 1)
                model = LinearRegression().fit(x_data, y_coords)
                slope, intercept = model.coef_[0], model.intercept_

                slope_transformed, intercept_transformed = transform_coefficients(slope)

                x_start, x_end = 0, square_size
                y_start, y_end = slope_transformed * x_start + intercept_transformed, slope_transformed * x_end + intercept_transformed
                x_start_global, y_start_global = x_start + i, y_start + j
                x_end_global, y_end_global = x_end + i, y_end + j

                regression_results.append((x_start_global, y_start_global, x_end_global, y_end_global))
            else:
                slope_transformed, intercept_transformed = 0, 1

            row_data.append(f"{i},{j},{slope_transformed},{intercept_transformed}")

    write_header = not os.path.exists(csv_filename)
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if write_header:
            writer.writerow(["image_name", "cubes_info"])
        writer.writerow(row_data)

def load_db(path):
    for lettres in os.listdir(path):
        letter_path = os.path.join(path, lettres)
        for lettre in os.listdir(letter_path):
            file_path = os.path.join(letter_path, lettre)
            with Image.open(file_path) as img:
                split_and_process_image(img, "squares", "cubes_info.csv", lettres, "sample_variable")

load_db(path='data')

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=2021)

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




mlp = MLPClassifier(hidden_layer_sizes=(32,), activation='relu', solver='adam', max_iter=1000, random_state=42)

mlp.fit(X_train, y_train)

train_score = mlp.score(X_train, y_train)
test_score = mlp.score(X_test, y_test)

y_pred = mlp.predict(X_test)

report = classification_report(y_test, y_pred, target_names=[f"Classe {i}" for i in range(6)])

print(report)

best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

metrics = {
    "train_score": round(best_model.score(X_train, y_train),2),
    "test_score":round(best_model.score(X_test, y_test),2),
    "classification_report": classification_report(y_test, y_pred, target_names=[f"Classe {i}" for i in range(6)], output_dict=True),
}

print(metrics)

with open("best_mlp_model.pkl", "wb") as file:
    pickle.dump({"model": best_model, "metrics": metrics}, file)

print("model.pkl'")