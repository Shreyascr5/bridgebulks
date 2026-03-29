import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function Profile() {
  const [profile, setProfile] = useState({});
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem("token");

      const res1 = await axios.get("http://127.0.0.1:8000/customers/me", {
        headers: { Authorization: `Bearer ${token}` },
      });

      const res2 = await axios.get("http://127.0.0.1:8000/bulk-orders/my-orders", {
        headers: { Authorization: `Bearer ${token}` },
      });

      setProfile(res1.data);
      setOrders(res2.data);
    };

    fetchProfile();
  }, []);

  const totalSpent = orders.reduce((sum, o) => sum + o.total_price, 0);

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>User Profile</h2>

        <div className="card p-3 mt-3">
          <h5>Email: {profile.email}</h5>
          <p>Total Orders: {orders.length}</p>
          <p>Total Spent: ₹{totalSpent}</p>
        </div>
      </div>
    </div>
  );
}

export default Profile;