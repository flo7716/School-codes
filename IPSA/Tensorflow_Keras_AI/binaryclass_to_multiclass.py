# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:58:59 2023

@author: flori
"""

import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt

def training_test_dataset_multi_class(nb_points=1000, lim=10):
    """
    Génère nb_points pour les ensembles de données d'entraînement et de test
    Les étiquettes correspondantes sont également générées
    Les coordonnées des points 2D vont de -lim à +lim
    Les ensembles de données et les étiquettes sont stockés dans des tableaux numpy
    """
    x = []
    y = []
    
    for i in range(nb_points):
        point = [np.random.uniform(-lim, lim), np.random.uniform(-lim, lim)]
        x.append(point)
        
        if point[0] < 0 and point[1] < 0:
            y.append([1, 0, 0, 0])
        elif point[0] > 0 and point[1] > 0:
            y.append([0, 1, 0, 0])
        elif point[0] < 0:
            if abs(point[0]) < point[1] or abs(point[0]) == point[1]:
                y.append([0, 1, 0, 0])
            else:
                y.append([0, 0, 1, 0])
        elif point[1] < 0:
            if point[0] < abs(point[1]) or point[0] == abs(point[1]) :
                y.append([0, 0, 0, 1])
            else: 
                y.append([1, 0, 0, 0])

    draw_x = np.array(x)
    plt.scatter(draw_x[:, 0], draw_x[:, 1], cmap='hot')
    plt.show()
    
    return np.array(x), np.array(y)

def dataset_for_prediction_multi_class(nb_points=500, lim=100):
    """
    Génère un ensemble de données pour que le modèle puisse prédire leurs étiquettes lorsqu'il est entraîné
    Les points ont des coordonnées allant de -lim à +lim
    L'ensemble de données est stocké dans un tableau numpy
    """
    x_p = [[np.random.uniform(-lim, lim), np.random.uniform(-lim, lim)] for i in range(nb_points)]
    return np.array(x_p)

# Préparation des données
X, y = training_test_dataset_multi_class()
nb_train = 900
x_train, y_train = X[:nb_train], y[:nb_train]
x_test, y_test = X[nb_train:], y[nb_train:]

# Construction du modèle
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(2,1)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(4, activation="softmax")  # Modification ici pour 4 classes
])

# Compilation du modèle
model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.001, momentum=0.9),
    loss="categorical_crossentropy",  # Modification ici pour la classification multi-classe
    metrics=["accuracy"]
)

# Entraînement du modèle
history = model.fit(x_train, y_train, validation_split=0.2, epochs=30, verbose=2)

# Évaluation du modèle
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

# Prédiction des étiquettes
x_p = dataset_for_prediction_multi_class()
predicted_labels = model.predict(x_p)

# Affichage des courbes de perte
epochs = range(len(history.history["loss"]))
plt.figure(1)
plt.plot(epochs, history.history["loss"])
plt.plot(epochs, history.history["val_loss"])
plt.title("Courbe de perte")

# Affichage de la précision
plt.figure(2)
plt.plot(epochs, history.history["accuracy"], label="Précision d'entraînement")
plt.plot(epochs, history.history["val_accuracy"], label="Précision de validation")
plt.title("Courbes de précision")
plt.legend()

# Affichage de la prédiction
plt.figure(3)
plt.scatter(x_p[:, 0], x_p[:, 1], c=np.argmax(predicted_labels, axis=1), cmap="viridis")  # Utilisation de argmax pour obtenir la classe prédite
plt.title("Prédiction des étiquettes")
plt.show()

print("Perte de test:", test_loss)
print("Précision de test:", test_acc)