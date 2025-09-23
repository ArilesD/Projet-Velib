import json


file_path = "station_information.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)


def extraire_infos(stations):
    """Extrait uniquement les informations essentielles des stations."""
    donnees_filtrees = []
    for station in stations:
        donnees_filtrees.append({
            "station_id": station["station_id"],
            "name": station["name"],
            "capacity": station["capacity"],
            "lat": station["lat"],
            "lon": station["lon"]
        })
    return donnees_filtrees


if "data" in data and "stations" in data["data"]:
    stations = data["data"]["stations"]
    donnees_filtrees = extraire_infos(stations)


    formatted_file_path = "velib_stations.json"
    with open(formatted_file_path, "w", encoding="utf-8") as f:
        json.dump(donnees_filtrees, f, indent=4, ensure_ascii=False)

    print(f"Données enregistrées sous : {formatted_file_path}")
else:
    print("Données invalides ou indisponibles.")


