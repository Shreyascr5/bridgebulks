import { useEffect, useState } from "react";
import axios from "axios";

function Profile() {
  const [profile, setProfile] = useState({});
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchProfile = async () => {
      // This demo UI keeps customer/auth logic minimal.
      // Backend's order-history demo endpoint is available without auth.
      try {
        const ordersRes = await axios.get("/bulk-orders/my-orders");
        setOrders(ordersRes.data || []);
      } catch {
        setOrders([]);
      }

      // Show a friendly placeholder profile for the presentation.
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