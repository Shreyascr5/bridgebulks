import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function OrderStatus() {
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      // Order status update isn't fully implemented in the current backend model.
      // For demo purposes, we reuse the "my-orders" endpoint.
      const res = await axios.get("/bulk-orders/my-orders");
      setOrders(res.data || []);
    } catch (e) {
      setError("Could not load orders.");
      setOrders([]);
    }
  };

  return (
    <div>
      <Navbar />
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
    </div>
  );
}

export default OrderStatus;