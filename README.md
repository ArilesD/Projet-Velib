# Vélib’ - Cartographie des stations

Projet universitaire réalisé en équipe à partir d’un instantané de **1 473 stations Vélib’** à Paris et dans les communes voisines.

Les cartes montrent les stations, leurs voisines et les zones géométriquement les plus proches de chacune.

**Outils :** Python, Folium, NumPy et SciPy.

## Aperçu du projet

![Cartes de Delaunay, de Kruskal et de Voronoï sur les 1 473 stations.](docs/presentation.gif)

Les cartes utilisent un instantané des stations, sans disponibilité des vélos en temps réel.

[Image en grand format](docs/apercu.png) · [Voir la vidéo](docs/presentation.mp4)

## Ouvrir les cartes

- [Carte des stations et de leurs voisines](https://arilesd.github.io/Projet-Velib/velib_stations_map.html).
- [Carte des cellules de Voronoï](https://arilesd.github.io/Projet-Velib/velib_stations_voronoi.html).

Le menu en haut à droite permet de choisir les éléments affichés :

- **Delaunay** relie les stations voisines par des triangles.
- **Kruskal** relie les stations par un arbre de longueur totale minimale.
- **Voronoï** dessine les zones les plus proches de chaque station. Les cellules ouvertes aux limites du réseau sont omises.

Les couleurs représentent le rapport entre la capacité d’une station et son nombre de voisines. Elles ne représentent pas le nombre de vélos disponibles. Les cartes décrivent une proximité géométrique ; elles ne mesurent pas les temps de trajet.

## Télécharger et lancer

1. Installe [Python 3.14](https://www.python.org/downloads/) si besoin, en cochant **Add python.exe to PATH**.
2. [Télécharge le projet en ZIP](https://github.com/ArilesD/Projet-Velib/archive/refs/heads/main.zip), fais **Extraire tout**, puis ouvre le dossier extrait.
3. Double-clique sur **LANCER.cmd**.

Le premier lancement nécessite Internet pour installer les bibliothèques. Garde la fenêtre de lancement ouverte pendant l’utilisation et appuie sur **Entrée** dans cette fenêtre pour arrêter le projet.

Le lancement ouvre les cartes déjà calculées. Les composants et les limites des départements sont fournis ; le fond OpenStreetMap nécessite Internet.

## Sources des données

Les cartes utilisent un instantané des coordonnées et capacités des stations du **20 janvier 2025**. [Données publiques Vélib’](https://www.data.gouv.fr/datasets/velib-localisation-et-caracteristique-des-stations).

Les limites des départements proviennent d’IGN Admin Express COG 2018, via France GeoJSON, sous Licence Ouverte. [Source des contours](https://github.com/gregoiredavid/france-geojson#licence).

Fond de carte © [les contributeurs OpenStreetMap](https://www.openstreetmap.org/copyright).
