import { useEffect, useState } from "react";
import API from "../api";
import Navbar from "../components/Navbar";

function OrderStatus() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    const res = await API.get("/order-status/");
    setOrders(res.data);
  };

  const updateStatus = async (orderId, status) => {
    await API.put(`/order-status/${orderId}`, { status });
    fetchOrders();
  };

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>Order Status Tracking</h2>

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
                <td>{o.vendor_name}</td>
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
                  <button
                    className="btn btn-sm btn-warning me-2"
                    onClick={() => updateStatus(o.order_id, "Shipped")}
                  >
                    Ship
                  </button>
                  <button
                    className="btn btn-sm btn-success"
                    onClick={() => updateStatus(o.order_id, "Delivered")}
                  >
                    Deliver
                  </button>
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