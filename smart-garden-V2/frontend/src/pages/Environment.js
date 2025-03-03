import React, { useEffect, useState } from "react";
import axios from "axios";
import GaugeChart from "react-gauge-chart";
import "../App.css";

function Environment() {
    const [environmentScore, setEnvironmentScore] = useState(0);

    useEffect(() => {
        axios.get("http://127.0.0.1:5001/environment")
            .then(response => {
                setEnvironmentScore(response.data.score);
            })
            .catch(error => {
                console.error("Fehler beim Laden der Umweltbewertung:", error);
            });
    }, []);

    return (
        <div className="container">
            <h1>🌍 Umweltbewertung</h1>
            <p>Wie gut sind die aktuellen Bedingungen für deine Pflanzen?</p>
            <div className="chart-container">
                <GaugeChart 
                    id="gauge-chart"
                    nrOfLevels={5}
                    percent={environmentScore / 100}
                    colors={["#ff0000", "#ff9900", "#ffff00", "#99cc00", "#00ff00"]}
                    textColor="#000"
                />
            </div>
        </div>
    );
}

export default Environment;