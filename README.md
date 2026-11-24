# Vélib’ - Cartographie des stations et de leurs voisines

Projet universitaire réalisé en équipe : cartographie de **1 473 stations Vélib’** à Paris et dans les communes voisines. À partir de leurs coordonnées et de leur capacité, deux cartes explorent la disposition des stations et leur voisinage.

## Aperçu du projet

![Delaunay, arbre de Kruskal et cellules de Voronoï sur l’instantané des 1 473 stations fourni dans ce dépôt.](docs/presentation.gif)

Delaunay, arbre de Kruskal et cellules de Voronoï sur l’instantané des 1 473 stations fourni dans ce dépôt.

[Voir la capture en grand format](docs/apercu.png) · [Voir la vidéo en grand format](docs/presentation.mp4) · [Mon parcours et mes autres projets](https://github.com/ArilesD)

## Télécharger et lancer

1. [Télécharge le ZIP complet](https://github.com/ArilesD/Projet-Velib/archive/refs/heads/main.zip).
2. Dans l’Explorateur de fichiers, fais **Extraire tout**, puis ouvre le dossier extrait.
3. Installe [Python 3.14](https://www.python.org/downloads/) si besoin, en cochant **Add python.exe to PATH**. Double-clique ensuite sur **LANCER.cmd**.

Le lancement ouvre les cartes déjà calculées depuis l’instantané des 1 473 stations. [Carte des stations](http://127.0.0.1:5115/velib_stations_map.html) · [Carte de Voronoï](http://127.0.0.1:5115/velib_stations_voronoi.html)

Garde la fenêtre de lancement ouverte pendant l’utilisation. Appuie sur **Entrée** dans cette fenêtre pour arrêter le projet. La première préparation des applications Python installe les bibliothèques depuis Internet. Les ouvertures suivantes réutilisent l’installation du dossier.


## Explorer les cartes

- [Ouvrir la carte des stations et du réseau géométrique](https://arilesd.github.io/Projet-Velib/velib_stations_map.html) - Les triangles verts relient les stations voisines selon la triangulation de Delaunay. Les arêtes noires forment un arbre couvrant de poids minimal calculé avec l’algorithme de Kruskal.
- [Ouvrir la carte de Voronoï](https://arilesd.github.io/Projet-Velib/velib_stations_voronoi.html) - Chaque cellule affichée correspond à la zone géométriquement la plus proche de sa station. Les cellules ouvertes aux limites du réseau sont omises.

Le menu en haut à droite permet d’afficher les stations, la triangulation, l’arbre ou les cellules selon la carte. Les composants de la carte et les limites des départements sont fournis dans le dossier. Le fond OpenStreetMap nécessite Internet. [Fond de carte © les contributeurs OpenStreetMap](https://www.openstreetmap.org/copyright)

Pour garder une copie sur ton ordinateur, télécharge le ZIP complet et ouvre les cartes avec **LANCER.cmd**. [Fichier des stations](velib_stations_map.html) · [Fichier de Voronoï](velib_stations_voronoi.html)

## Lire les couleurs

Le projet divise la capacité d’une station par le nombre de ses voisines dans la triangulation de Delaunay. La première carte colore ce ratio selon une échelle continue. La carte de Voronoï le classe autour d’un seuil de 6 choisi pour le projet.

Les calculs reposent sur les coordonnées et la capacité des stations. Les cellules décrivent la proximité géométrique. Une analyse de la desserte demanderait aussi des données d’usage et des temps de trajet.

## Données

Le dépôt contient un instantané de `station_information.json`. Le fichier porte l’horodatage du **20 janvier 2025 à 21 h 52, heure de Paris**. Il fournit l’identifiant, le nom, la latitude, la longitude et la capacité des stations. Le format correspond au flux public de localisation Vélib’ Métropole. [Données publiques Vélib’ - Smovengo / Syndicat Autolib’ Vélib’ Métropole](https://www.data.gouv.fr/datasets/velib-localisation-et-caracteristique-des-stations)

## Régénérer les cartes

Depuis la racine du dépôt, utilise Python 3.12 à 3.14 et installe les dépendances. Les scripts lisent directement l’instantané d’origine station_information.json.

```powershell
python -m pip install -r requirements.txt
python carte.py
python carte_voronoi
```

Les cartes sont enregistrées dans velib_stations_map.html et velib_stations_voronoi.html.

Les limites locales des départements sont issues d’IGN Admin Express COG 2018, via France GeoJSON, sous Licence Ouverte. [Source des contours](https://github.com/gregoiredavid/france-geojson#licence)
