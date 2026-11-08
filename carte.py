import json
import numpy as np
import folium
from scipy.spatial import Delaunay
from collections import defaultdict
import math

# Chargement des données
with open("velib_coordonnées.json", encoding="utf-8") as f:
    coords = json.load(f)

with open("velib_stations.json", encoding="utf-8") as f:
    stations_info = json.load(f)

# Dictionnaires utiles
coord_to_id = {(s['lat'], s['lon']): s['station_id'] for s in coords}
capacites = {s['station_id']: s['capacity'] for s in stations_info}
id_to_coord = {s['station_id']: (s['lat'], s['lon']) for s in coords}

# Points pour Delaunay
points = np.array([(s['lat'], s['lon']) for s in coords])
tri = Delaunay(points)

# Construction de la liste d’adjacence
adjacence = defaultdict(set)
edges = set()
for simplex in tri.simplices:
    for i in range(3):
        for j in range(i + 1, 3):
            idx1, idx2 = simplex[i], simplex[j]
            id1 = coord_to_id[tuple(points[idx1])]
            id2 = coord_to_id[tuple(points[idx2])]
            adjacence[id1].add(id2)
            adjacence[id2].add(id1)
            # Stocker l'arête avec la distance comme poids
            lat1, lon1 = points[idx1]
            lat2, lon2 = points[idx2]
            dist = math.dist((lat1, lon1), (lat2, lon2))
            edges.add((dist, id1, id2))

# Calcul de l’indice de répartition
indices = {}
for station_id in adjacence:
    capacite = capacites.get(station_id, 1)
    voisins = len(adjacence[station_id])
    indice = capacite / voisins if voisins != 0 else 0
    indices[station_id] = indice

# Normalisation des couleurs (rouge → vert)
max_indice = max(indices.values())
min_indice = min(indices.values())

def indice_to_color(indice):
    ratio = (indice - min_indice) / (max_indice - min_indice)
    r = int(255 * (1 - ratio))
    g = int(255 * ratio)
    return f"#{r:02x}{g:02x}00"

# Algorithme de Kruskal pour l'arbre couvrant minimum
parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX

# Initialisation des parents
for s in adjacence:
    parent[s] = s

# Tri des arêtes par poids croissant
sorted_edges = sorted(edges)
acm_edges = []

for dist, a, b in sorted_edges:
    if find(a) != find(b):
        union(a, b)
        acm_edges.append((a, b))

# Création de la carte
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
m.fit_bounds([points.min(axis=0).tolist(), points.max(axis=0).tolist()], padding=(20, 20))
triangles = folium.FeatureGroup(name="Triangulation de Delaunay").add_to(m)
stations = folium.FeatureGroup(name="Stations").add_to(m)
arbre = folium.FeatureGroup(name="Arbre couvrant (Kruskal)", show=False).add_to(m)

# Ajout des triangles en vert
for simplex in tri.simplices:
    p1, p2, p3 = points[simplex]
    folium.PolyLine([p1, p2, p3, p1], color="green", weight=1, opacity=0.4).add_to(triangles)

# Ajout des stations avec couleur selon l’indice
for station in coords:
    station_id = station['station_id']
    if station_id in indices:
        couleur = indice_to_color(indices[station_id])
        folium.CircleMarker(
            location=[station['lat'], station['lon']],
            radius=3,
            color=couleur,
            fill=True,
            fill_color=couleur,
            fill_opacity=0.9,
            popup=f"Station {station_id}<br>Capacité / nombre de voisines : {indices[station_id]:.2f}"
        ).add_to(stations)

# Ajout des arêtes de l'arbre couvrant minimum en noir
for a, b in acm_edges:
    latlon_a = id_to_coord[a]
    latlon_b = id_to_coord[b]
    folium.PolyLine([latlon_a, latlon_b], color="black", weight=1.5).add_to(arbre)

# Ajout de la légende
legend_html = """
<div style="
    position: fixed;
    bottom: 28px; left: 12px; width: 285px; max-width: calc(100% - 44px);
    background-color: white; z-index:9999;
    border:2px solid grey; padding:10px; font-size:14px;
">
<b>Légende :</b><br>
<span style='color:green;'>─</span> Triangle de Delaunay<br>
<span style='color:black;'>─</span> Arbre couvrant minimum (Kruskal)<br>
<span style='color:red;'>●</span> Ratio capacité / voisines faible<br>
<span style='color:green;'>●</span> Ratio capacité / voisines élevé
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))
folium.LayerControl(collapsed=False).add_to(m)

# Sauvegarde
m.save("velib_stations_map.html")
print("Carte mise à jour avec l’indice de répartition et l'arbre couvrant minimum.")
