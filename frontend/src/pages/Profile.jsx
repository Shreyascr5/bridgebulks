import { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function Profile() {
  const [profile, setProfile] = useState({});
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const ordersRes = await axios.get(`${API_BASE_URL}/bulk-orders/my-orders`);
        setOrders(ordersRes.data || []);
      } catch {
        setOrders([]);
      }
      setProfile({ email: "demo@bridgebulks.com" });
    };
    fetchProfile();
  }, []);

  const totalSpent = orders.reduce((sum, o) => sum + o.total_price, 0);

  return (
    <div className="container mt-4">
        <h2>User Profile</h2>

        <div className="card p-3 mt-3">
          <h5>Email: {profile.email}</h5>
          <p>Total Orders: {orders.length}</p>
          <p>Total Spent: ₹{totalSpent}</p>
        </div>
      </div>
  );
}

export default Profile;