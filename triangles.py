import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Chargement des coordonnées des stations depuis un fichier JSON
with open("velib_coordonnées.json", "r") as file:
    stations_json = json.load(file)

# Extraction des coordonnées
points = np.array([(station["lon"], station["lat"]) for station in stations_json])

# Calcul de la triangulation de Delaunay
tri = Delaunay(points)

# Tracé de la triangulation
plt.figure(figsize=(50, 50))  # Dézoomer en augmentant la taille de la figure
plt.triplot(points[:, 0], points[:, 1], tri.simplices, color='blue')
plt.plot(points[:, 0], points[:, 1], 'ro', label='Stations')

# Ajout des labels
#

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Triangulation de Delaunay des stations")
plt.legend()
plt.show()