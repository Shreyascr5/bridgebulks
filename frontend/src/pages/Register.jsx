import { useState } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API_BASE_URL}/auth/register`, {
        name,
        email,
        password,
      });
      alert("Registered! Please login.");
      window.location.hash = "#/login";
    } catch (err) {
      alert("Registration failed. Email may already be in use.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-4">
          <div className="card p-4 shadow">
            <h3 className="text-center mb-3">Register</h3>

            <form onSubmit={handleRegister}>
              <input
                className="form-control mb-2"
                placeholder="Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
              />
              <input
                className="form-control mb-2"
                placeholder="Email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
              <input
                type="password"
                className="form-control mb-2"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
              <button type="submit" className="btn btn-success w-100">
                Register
              </button>
            </form>

            <p className="mt-3 text-center">
              Already registered? <a href="#/login">Login</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Register;