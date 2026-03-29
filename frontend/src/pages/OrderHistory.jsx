import { useEffect, useState } from "react";
import axios from "axios";

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

  return (
    <div>
      <h2>Order History</h2>

      {orders.map((order) => (
        <div key={order.order_id}>
          <p>Order ID: {order.order_id}</p>
          <p>Total Price: {order.total_price}</p>

          <h4>Items:</h4>
          {order.items.map((item, index) => (
            <div key={index}>
              <p>Product ID: {item.product_id}</p>
              <p>Vendor ID: {item.vendor_id}</p>
              <p>Quantity: {item.quantity}</p>
            </div>
          ))}
          <hr />
        </div>
      ))}
    </div>
  );
}

export default OrderHistory;