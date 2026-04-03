import { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function CreateOrder() {
  const [products, setProducts] = useState([]);
  const [items, setItems] = useState([{ product_id: "", quantity: "1" }]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const res = await axios.get(`${API_BASE_URL}/products/`);
        setProducts(res.data || []);
      } catch {
        setProducts([]);
      }
    };
    fetchProducts();
  }, []);

  const addItem = () => {
    setItems([...items, { product_id: "", quantity: "" }]);
  };

  const updateItem = (index, field, value) => {
    const newItems = [...items];
    newItems[index][field] = value;
    setItems(newItems);
  };

  const createOrder = async () => {
    try {
      for (const item of items) {
        if (!item.product_id) continue;
        const qty = parseInt(item.quantity, 10);
        if (!Number.isFinite(qty) || qty <= 0) continue;

        const product = products.find((p) => String(p.id) === String(item.product_id));
        if (!product) continue;

        await axios.post(`${API_BASE_URL}/bulk-orders/`, {
          product_id: parseInt(item.product_id, 10),
          quantity: qty,
          total_price: product.price * qty,
        });
      }
      alert("Order(s) Created!");
    } catch {
      alert("Failed to create order(s).");
    }
  };

  return (
    <div className="container mt-4">
      <h2>Create Bulk Order</h2>

      {items.map((item, index) => (
        <div className="row mt-2" key={index}>
          <div className="col">
            <select
              className="form-control"
              onChange={(e) => updateItem(index, "product_id", e.target.value)}
            >
              <option value="">Select Product</option>
              {products.map((p) => (
                <option key={p.id} value={p.id}>
                  {p.name}
                </option>
              ))}
            </select>
          </div>

          <div className="col">
            <input
              className="form-control"
              placeholder="Quantity"
              value={item.quantity}
              onChange={(e) => updateItem(index, "quantity", e.target.value)}
            />
          </div>
        </div>
      ))}

      <button className="btn btn-secondary mt-3" onClick={addItem}>
        Add Product
      </button>

      <button className="btn btn-dark mt-3 ms-2" onClick={createOrder}>
        Create Order
      </button>
    </div>
  );
}

export default CreateOrder;
