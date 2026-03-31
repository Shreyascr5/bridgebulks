import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function OrderHistory() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const res = await axios.get("/bulk-orders/my-orders");
        setOrders(res.data || []);
      } catch (e) {
        setOrders([]);
      }
    };

    fetchOrders();
  }, []);

  const getStatusColor = (status) => {
    if (status === "Placed") return "secondary";
    if (status === "Processing") return "warning";
    if (status === "Shipped") return "primary";
    if (status === "Delivered") return "success";
    return "secondary";
  };

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>Order History</h2>

        {orders.length === 0 ? (
          <div className="alert alert-info mt-3">No orders yet.</div>
        ) : (
          orders.map((order) => (
            <div className="card p-3 mt-3" key={order.order_id}>
              <h5>Order ID: {order.order_id}</h5>
              <p>
                Product: {order.product_name || order.product_id} | Qty: {order.quantity}
              </p>
              <p>Total Price: ₹{order.total_price}</p>

              <span className={`badge bg-${getStatusColor(order.status)}`}>
                {order.status}
              </span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default OrderHistory;