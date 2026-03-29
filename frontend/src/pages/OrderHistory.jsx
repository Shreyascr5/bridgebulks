import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function OrderHistory() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      const token = localStorage.getItem("token");

      const res = await axios.get("http://127.0.0.1:8000/bulk-orders/my-orders", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setOrders(res.data);
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

        {orders.map((order) => (
          <div className="card p-3 mt-3" key={order.order_id}>
            <h5>Order ID: {order.order_id}</h5>
            <p>Total Price: ₹{order.total_price}</p>

            <span className={`badge bg-${getStatusColor(order.status)}`}>
              {order.status}
            </span>

            <hr />
            <h6>Items:</h6>
            {order.items.map((item, index) => (
              <div key={index}>
                Product ID: {item.product_id} | Vendor ID: {item.vendor_id} | Qty: {item.quantity}
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}

export default OrderHistory;