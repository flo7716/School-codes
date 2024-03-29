#Florian ANDRE
#2B DIA
#Liste des bibliotheques

import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

# Scénario 1 : Liaison simple
# Etape 1 : Créer un ensemble de données aléatoire avec 15 points
np.random.seed(0)  # Pour la reproductibilité
data = np.random.rand(15, 2)

# Etape 2 : Ajouter 4 valeurs aberrantes
outliers = np.array([[0.1, 1.0], [0.9, 0.2], [1.5, 0.9], [1.8, 0.1]])
data = np.vstack((data, outliers))

# Etape 3 : Calculer les distances euclidiennes par paire
distance_matrix = pdist(data) # On utilise pdist pour obtenir une matrice de distance condensée

# Etape 4 : Effectuer une classification hiérarchique avec la méthode de liaison "simple"
linkage_matrix = linkage(distance_matrix, method='single')

# Etape 5 : Créer un dendrogramme pour visualiser les clusters
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix, labels=range(len(data)), leaf_rotation=90, leaf_font_size=12)
plt.title("Classification Hiérarchique (Liaison simple)")
plt.xlabel("Points de Données")
plt.ylabel("Distance")
plt.show()

# Scénario 2 : Liaison complete
# Etape 6 : Calculer la liaison en utilisant la méthode de liaison complète
linkage_matrix_complete = linkage(distance_matrix, method='complete')

# Etape 7 : Création du dendrogramme pour la liaison complète
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix_complete, labels=range(len(data)), leaf_rotation=90, leaf_font_size=12)
plt.title("Classification Hiérarchique (Liaison complète)")
plt.xlabel("Points de Données")
plt.ylabel("Distance")
plt.show()
