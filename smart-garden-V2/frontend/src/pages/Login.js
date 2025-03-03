import React, { useState } from "react";
import axios from "axios";
import "../App.css";

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");

    const handleLogin = () => {
        axios.post("http://127.0.0.1:5001/auth/login", { username, password })
            .then(response => {
                setMessage("Login erfolgreich! ✅");
            })
            .catch(error => {
                setMessage("Login fehlgeschlagen. ❌");
            });
    };

    return (
        <div className="container">
            <h1>🔑 Login</h1>
            <input 
                type="text" 
                placeholder="Benutzername" 
                value={username} 
                onChange={(e) => setUsername(e.target.value)} 
            />
            <input 
                type="password" 
                placeholder="Passwort" 
                value={password} 
                onChange={(e) => setPassword(e.target.value)} 
            />
            <button onClick={handleLogin}>Anmelden</button>
            <p>{message}</p>
        </div>
    );
}

export default Login;