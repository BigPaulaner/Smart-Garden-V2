import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Explore from "./pages/Explore";
import MyGarden from "./pages/MyGarden";
import Login from "./pages/Login";
import Environment from "./pages/Environment";
import "./App.css";

function App() {
    return (
        <Router>
            <div className="app-container">
                {/* Navigation */}
                <nav className="navbar">
                    <ul>
                        <li><Link to="/">🏡 Home</Link></li>
                        <li><Link to="/explore">🌿 Explore</Link></li>
                        <li><Link to="/my-garden">🪴 My Garden</Link></li>
                        <li><Link to="/environment">🌍 Umwelt</Link></li>
                        <li><Link to="/login">🔑 Login</Link></li>
                    </ul>
                </nav>

                {/* Hauptinhalt */}
                <div className="container">
                    <Routes>
                        <Route path="/" element={
                            <div>
                                <h1>🌱 Willkommen bei Smart Garden!</h1>
                                <p>Hier kannst du Pflanzen entdecken, deinen Garten verwalten und Umweltbedingungen checken.</p>
                            </div>
                        } />
                        <Route path="/explore" element={<Explore />} />
                        <Route path="/my-garden" element={<MyGarden />} />
                        <Route path="/environment" element={<Environment />} />
                        <Route path="/login" element={<Login />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;