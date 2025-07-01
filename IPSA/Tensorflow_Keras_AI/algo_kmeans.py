# Florian ANDRE 
# 2B DIA
# Liste des bibilotheques

import numpy as np
import matplotlib.pyplot as plt
import random

#Etape 1 : chargement des donnees

np.random.seed(0)
points=np.random.rand(30,2)

#Etape 2 : initialisation
def initialization_centroids(points,k,random=False):
    if random:
        return points[np.random.choice(points.shape[0],k,replace=False)]
    else:
        return points[:k]

#Nombre de clusters
k=2
centroids=initialization_centroids(points,k,random=False)

#Etape 3 : assignation a un cluster
def cluster_assignation(points,centroids):
    distances=np.linalg.norm(points[:,np.newaxis]-centroids,axis=2)
    return np.argmin(distances, axis=1)

clusters=cluster_assignation(points,centroids)

#Etape 4 : mise a jour des centroids
def update_centroids(points,clusters,k):
    new_centroids=np.zeros((k,points.shape[1]))
    for i in range(k):
        new_centroids[i]=np.mean(points[clusters == i],axis=0)
    return new_centroids

#Etape 5 : seuil de convergence
epsilon=0.001

#Etape 6 : Repetition jusqu'au nombre limite de convergence ou d'iterations
Nitermax=25
for iter in range(Nitermax):
    new_clusters=cluster_assignation(points,centroids)
    if np.all(clusters == new_clusters):
        print(f"Convergence atteinte apres {iter + 1} iterations.\n")
        break
    centroids = update_centroids(points,new_clusters,k)
    clusters = new_clusters

#Etape 7 : mise en forme sur le graphique
colors=['b','g','r','c','m','y','k']
plt.figure(figsize=(8,6))
for i in range(k):
    cluster_points=points[clusters == i]
    plt.scatter(cluster_points[:,0],cluster_points[:,1],c=colors[i],label=f'Cluster {i+1}')
    plt.scatter(centroids[i,0],centroids[i,1],c=colors[i],marker='x',s=100,label=f'Centroid {i+1}')
plt.title('K-Means clustering')
plt.legend()
plt.show()

#Etape 8 : Comparaison des resultats
print("Final Clusters : ",clusters)
print("Final Centroids : ",centroids)
