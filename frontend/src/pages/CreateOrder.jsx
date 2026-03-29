import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function CreateOrder() {
  const [products, setProducts] = useState([]);
  const [items, setItems] = useState([{ product_id: "", quantity: "" }]);

  useEffect(() => {
    const fetchProducts = async () => {
      const res = await axios.get("http://127.0.0.1:8000/products/");
      setProducts(res.data);
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
    const token = localStorage.getItem("token");

    const res = await axios.post(
      "http://127.0.0.1:8000/bulk-orders/",
      { items },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    alert("Order Created! Total Price: " + res.data.total_price);
  };

  return (
    <div>
      <Navbar />

      <div className="container mt-4">
        <h2>Create Bulk Order</h2>

        {items.map((item, index) => (
          <div className="row mt-2" key={index}>
            <div className="col">
              <select
                className="form-control"
                onChange={(e) =>
                  updateItem(index, "product_id", e.target.value)
                }
              >
                <option>Select Product</option>
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
                onChange={(e) =>
                  updateItem(index, "quantity", e.target.value)
                }
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
    </div>
  );
}

export default CreateOrder;