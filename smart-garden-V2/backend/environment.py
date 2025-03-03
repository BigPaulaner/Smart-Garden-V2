import requests
from flask import Blueprint, request, jsonify

environment_bp = Blueprint("environment", __name__)

@environment_bp.route("/environment", methods=["GET"])
def get_environmental_score():
    zip_code = request.args.get("zip", default="10115", type=str)

    # Wetter abrufen
    weather_response = requests.get(f"http://127.0.0.1:5001/weather?zip={zip_code}")
    weather = weather_response.json()

    # Bodenbeschaffenheit abrufen
    soil_response = requests.get(f"http://127.0.0.1:5001/soil?zip={zip_code}")
    soil = soil_response.json()

    # Bewertung berechnen (1-100 Skala)
    temp_score = max(0, min(100, (30 - abs(weather["temperature"] - 20)) * 3))
    rain_score = max(0, min(100, (15 - weather["rain"]) * 6))
    ph_score = 100 if 5.5 <= soil["pH_value"] <= 7.0 else 50

    total_score = (temp_score + rain_score + ph_score) / 3
    rating = "Sehr schlecht" if total_score < 30 else "Schlecht" if total_score < 50 else "Mittel" if total_score < 70 else "Gut" if total_score < 85 else "Sehr gut"

    return jsonify({
        "zip_code": zip_code,
        "total_score": total_score,
        "rating": rating
    })