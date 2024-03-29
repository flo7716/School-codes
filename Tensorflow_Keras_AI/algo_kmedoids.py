# Florian ANDRE 
# 2B DIA
#Liste des bibilotheques

import numpy as np
import matplotlib.pyplot as plt

#Etape 1 : chargement des donnees

np.random.seed(0)
points=np.random.rand(30,2)

#Etape 2 : initialisation des medoids 
def initialize_medoids(points, k, random=False):
    if random:
        return points[np.random.choice(points.shape[0], k, replace=False)]
    else:
        return points[:k]

k=2 #nombre de clusters
medoids=initialize_medoids(points,k,random=False)

#Etape 3 : assignation a un cluster
def assign_to_clusters(points, medoids):
    distances = np.linalg.norm(points[:, np.newaxis] - medoids, axis=2)
    return np.argmin(distances, axis=1)

clusters = assign_to_clusters(points, medoids)

#Etape 4 : Mise a jour des medoids
def update_medoids(points, clusters, k):
    new_medoids = np.copy(medoids)
    for i in range(k):
        cluster_points = points[clusters == i]
        total_distances = np.sum(np.linalg.norm(cluster_points[:, np.newaxis] - cluster_points, axis=2), axis=1)
        new_medoids[i] = cluster_points[np.argmin(total_distances)]
    return new_medoids

#Etape 5 : seuil de convergence
epsilon=0.001

#Etape 6 : repetition jusqu'au seuil de convergence ou jusqu'au nombre limite d'iterations
Nitermax = 25
for iteration in range(Nitermax):
    new_clusters = assign_to_clusters(points, medoids)
    if np.all(clusters == new_clusters):
        print(f"Converged after {iteration + 1} iterations.")
        break
    medoids = update_medoids(points, new_clusters, k)
    clusters = new_clusters
    
#Etape 7 : Mise sous forme graphique
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
plt.figure(figsize=(8, 6))
for i in range(k):
    cluster_points = points[clusters == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[i], label=f'Cluster {i+1}')
    plt.scatter(medoids[i, 0], medoids[i, 1], c=colors[i], marker='x', s=100, label=f'Medoid {i+1}')
plt.title('K-Medoids Clustering')
plt.legend()
plt.show()

#Etape 8 : Comparaison des resultats
print("Final Clusters:", clusters)
print("Final Medoids:", medoids)

