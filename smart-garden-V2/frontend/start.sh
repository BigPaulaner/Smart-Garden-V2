#!/bin/bash

# Backend starten
echo "🚀 Starte Backend..."
cd backend
source venv/bin/activate
python app.py &

# Warten, damit sich das Backend korrekt initialisiert
sleep 5

# Frontend starten
echo "🌿 Starte Frontend..."
cd ../frontend
npm start