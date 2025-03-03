import React, { useEffect, useState } from "react";
import axios from "axios";
import "../App.css";

function MyGarden() {
    const [myPlants, setMyPlants] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        axios.get("http://127.0.0.1:5001/my-garden")
            .then(response => {
                setMyPlants(response.data);
                setLoading(false);
            })
            .catch(error => {
                setError("Fehler beim Laden deiner Pflanzen.");
                setLoading(false);
            });
    }, []);

    return (
        <div className="container">
            <h1>🪴 Mein Garten</h1>
            {loading ? <p>Lade Pflanzen...</p> : null}
            {error ? <p className="error">{error}</p> : null}
            <ul>
                {myPlants.map((plant, index) => (
                    <li key={index}>{plant.name} - {plant.water} Wasserbedarf</li>
                ))}
            </ul>
        </div>
    );
}

export default MyGarden;