import requests
from flask import Blueprint, request, jsonify

soil_bp = Blueprint("soil", __name__)

OPENPLZ_API = "https://api.openplz.org/geocode?"

@soil_bp.route("/soil", methods=["GET"])
def get_soil_data():
    zip_code = request.args.get("zip", default="10115", type=str)
    
    # 1️⃣ Postleitzahl -> Koordinaten abrufen
    response = requests.get(f"{OPENPLZ_API}zip={zip_code}&country=DE")
    if response.status_code != 200:
        return jsonify({"error": "Fehler beim Abrufen der Standortdaten"}), 400

    location_data = response.json()
    lat, lon = location_data["latitude"], location_data["longitude"]

    # 2️⃣ Standardisierte Bodenwerte (Beispieldaten, falls API nicht verfügbar ist)
    SOIL_DATABASE = {
        "10115": {"soil_type": "Lehm", "pH": 6.5, "nutrients": "mittel"},
        "20095": {"soil_type": "Sand", "pH": 5.8, "nutrients": "niedrig"},
        "80331": {"soil_type": "Ton", "pH": 7.2, "nutrients": "hoch"},
    }

    soil_info = SOIL_DATABASE.get(zip_code, {"soil_type": "Unbekannt", "pH": 6.0, "nutrients": "mittel"})

    return jsonify({
        "zip_code": zip_code,
        "latitude": lat,
        "longitude": lon,
        "soil_type": soil_info["soil_type"],
        "pH_value": soil_info["pH"],
        "nutrient_level": soil_info["nutrients"]
    })