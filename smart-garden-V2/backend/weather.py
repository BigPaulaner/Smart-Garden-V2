import requests
import os
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

load_dotenv()
weather_bp = Blueprint("weather", __name__)

API_KEY = os.getenv("9ee773a33220459232298469d51a73cb")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@weather_bp.route("/weather", methods=["GET"])
def get_weather():
    zip_code = request.args.get("zip", default="10115", type=str)
    country_code = "DE"

    params = {
        "zip": f"{zip_code},{country_code}",
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return jsonify({"error": "Wetterdaten konnten nicht abgerufen werden"}), 400

    data = response.json()
    return jsonify({
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "rain": data.get("rain", {}).get("1h", 0)  # Regenmenge der letzten Stunde
    })