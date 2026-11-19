import json
from pathlib import Path

import folium


def creer_carte():
    carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12, tiles=None, prefer_canvas=True)
    carte.default_js = [
        ("leaflet", "assets/leaflet/leaflet.js"),
        ("jquery", "assets/jquery/jquery.min.js"),
    ]
    carte.default_css = [("leaflet_css", "assets/leaflet/leaflet.css")]

    limites = Path(__file__).with_name("assets") / "idf.geojson"
    folium.GeoJson(
        json.loads(limites.read_text(encoding="utf-8-sig")),
        name="Départements d’Île-de-France (hors ligne)",
        overlay=False,
        interactive=False,
        style_function=lambda feature: {
            "color": "#69727e", "weight": 1, "fillColor": "#f8fafc", "fillOpacity": 0.75
        },
    ).add_to(carte)
    carte.get_root().html.add_child(folium.Element(
        '<div style="position:fixed;right:0;bottom:20px;z-index:999;'
        'background:white;padding:2px 6px;font:11px sans-serif">'
        'Limites : IGN Admin Express COG 2018, '
        '<a href="https://github.com/gregoiredavid/france-geojson">France GeoJSON</a></div>'
    ))
    folium.TileLayer("OpenStreetMap", name="OpenStreetMap (Internet)", show=False).add_to(carte)
    return carte
