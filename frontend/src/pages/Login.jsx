import { useState } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(`${API_BASE_URL}/auth/login`, {
        email,
        password,
      });

      if (res.data && res.data.access_token) {
        localStorage.setItem("token", res.data.access_token);
      }
      alert("Login successful!");
      window.location.hash = "#/dashboard";
    } catch (err) {
      alert("Login failed. Please check your credentials.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-4">
          <div className="card p-4 shadow">
            <h3 className="text-center mb-3">BridgeBulks Login</h3>

            <form onSubmit={handleLogin}>
              <div className="mb-3">
                <label>Email</label>
                <input
                  type="email"
                  className="form-control"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>

              <div className="mb-3">
                <label>Password</label>
                <input
                  type="password"
                  className="form-control"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>

              <button type="submit" className="btn btn-primary w-100">
                Login
              </button>
            </form>

            <p className="mt-3 text-center">
              New user? <a href="#/register">Register</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
