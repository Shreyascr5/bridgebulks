import { useState } from "react";
import axios from "axios";

function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    await axios.post("/auth/register", {
  name,
  email,
  password
});

    alert("Registered! Please login.");
    window.location.href = "/login";
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
                onChange={(e) => setName(e.target.value)}
              />
              <input
                className="form-control mb-2"
                placeholder="Email"
                onChange={(e) => setEmail(e.target.value)}
              />
              <input
                type="password"
                className="form-control mb-2"
                placeholder="Password"
                onChange={(e) => setPassword(e.target.value)}
              />
              <button className="btn btn-success w-100">Register</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Register;