import React, { useEffect, useState } from "react";
import axios from "axios";
import "../App.css";

function Explore() {
    const [plants, setPlants] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        axios.get("http://127.0.0.1:5001/explore")
            .then(response => {
                setPlants(response.data);
                setLoading(false);
            })
            .catch(error => {
                setError("❌ Fehler: Pflanzen konnten nicht geladen werden.");
                setLoading(false);
            });
    }, []);

    return (
        <div className="container">
            <h1>🌿 Entdecke neue Pflanzen</h1>
            {loading && <p>Lade Pflanzen...</p>}
            {error && <p className="error">{error}</p>}
            <ul>
                {plants.map((plant, index) => (
                    <li key={index}>{plant.name} - {plant.sunlight} Lichtbedarf</li>
                ))}
            </ul>
        </div>
    );
}

export default Explore;