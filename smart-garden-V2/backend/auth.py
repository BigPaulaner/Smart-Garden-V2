from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    zip_code = data.get("zip_code")

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Benutzer existiert bereits"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password, zip_code=zip_code)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registrierung erfolgreich"}), 201