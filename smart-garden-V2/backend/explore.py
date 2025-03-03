import requests
from flask import Blueprint, request, jsonify

explore_bp = Blueprint("explore", __name__)

PLANT_DATABASE = [
    {"name": "Lavendel", "climate": "warm", "care": "low"},
    {"name": "Minze", "climate": "moderate", "care": "medium"},
    {"name": "Tomate", "climate": "moderate", "care": "high"},
    {"name": "Aloe Vera", "climate": "warm", "care": "low"},
    {"name": "Efeu", "climate": "cold", "care": "medium"}
]

@explore_bp.route("/explore", methods=["GET"])
def explore_plants():
    zip_code = request.args.get("zip", default="10115", type=str)
    care_level = request.args.get("care_level", default="medium", type=str)

    weather_response = requests.get(f"http://127.0.0.1:5001/weather?zip={zip_code}")
    weather = weather_response.json()

    recommended_plants = [
        plant for plant in PLANT_DATABASE
        if (plant["care"] == care_level or care_level == "any") and
           ((weather["temperature"] > 15 and plant["climate"] == "warm") or
            (5 <= weather["temperature"] <= 20 and plant["climate"] == "moderate") or
            (weather["temperature"] < 5 and plant["climate"] == "cold"))
    ]

    return jsonify({"recommended_plants": recommended_plants})