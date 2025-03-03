import requests
import os
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

load_dotenv()
plants_bp = Blueprint("plants", __name__)

TREFLE_API_KEY = os.getenv("kzDKUXmE_BtrWzxsWY3PNub7UcRA_H4zdsEqc6WQ29w")
TREFLE_SEARCH_URL = "https://trefle.io/api/v1/plants/search"

@plants_bp.route("/plants/search", methods=["GET"])
def search_plants():
    query = request.args.get("query", default="", type=str)
    params = {"q": query, "token": TREFLE_API_KEY}
    response = requests.get(TREFLE_SEARCH_URL, params=params)

    if response.status_code != 200:
        return jsonify({"error": "Fehler beim Abrufen der Pflanzendaten"}), 400

    data = response.json()
    return jsonify({"plants": [{"name": p["common_name"], "scientific_name": p["scientific_name"]} for p in data["data"]]})