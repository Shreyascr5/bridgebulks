import { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function OrderStatus() {
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const res = await axios.get(`${API_BASE_URL}/bulk-orders/my-orders`);
      setOrders(res.data || []);
    } catch (e) {
      setError("Could not load orders.");
      setOrders([]);
    }
  };

  return (
    <div className="container mt-4">
        <h2>Order Status Tracking</h2>

        {error && <div className="alert alert-warning mt-3">{error}</div>}

        <table className="table table-bordered mt-3">
          <thead>
            <tr>
              <th>Order ID</th>
              <th>Vendor</th>
              <th>Total Price</th>
              <th>Status</th>
              <th>Update</th>
            </tr>
          </thead>
          <tbody>
            {orders.map((o) => (
              <tr key={o.order_id}>
                <td>{o.order_id}</td>
                <td>{o.product_name || o.product_id}</td>
                <td>₹{o.total_price}</td>
                <td>
                  <span
                    className={
                      o.status === "Pending"
                        ? "badge bg-warning"
                        : o.status === "Shipped"
                        ? "badge bg-info"
                        : o.status === "Delivered"
                        ? "badge bg-success"
                        : "badge bg-secondary"
                    }
                  >
                    {o.status}
                  </span>
                </td>
                <td>
                  <span className="text-muted">N/A</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
  );
}

export default OrderStatus;