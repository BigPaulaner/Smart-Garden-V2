from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from extensions import db
from auth import auth_bp
from plants import plants_bp
from weather import weather_bp
from soil import soil_bp
from environment import environment_bp
from explore import explore_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

# API-Routen registrieren
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(plants_bp, url_prefix="/plants")
app.register_blueprint(weather_bp, url_prefix="/weather")
app.register_blueprint(soil_bp, url_prefix="/soil")
app.register_blueprint(environment_bp, url_prefix="/environment")
app.register_blueprint(explore_bp, url_prefix="/explore")

@app.route("/")
def home():
    return jsonify({"message": "Backend läuft erfolgreich!"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)