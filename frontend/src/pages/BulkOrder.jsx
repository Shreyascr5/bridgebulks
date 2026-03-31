import { useEffect, useMemo, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function BulkOrder() {
  const [products, setProducts] = useState([]);
  const [productId, setProductId] = useState("");
  const [quantity, setQuantity] = useState("1");

  useEffect(() => {
    axios
      .get("/products/")
      .then((res) => {
        setProducts(res.data || []);
        if (res.data && res.data.length > 0) {
          setProductId(String(res.data[0].id));
        }
      })
      .catch(() => {
        setProducts([]);
      });
  }, []);

  const selectedProduct = useMemo(
    () => products.find((p) => String(p.id) === String(productId)) || null,
    [products, productId]
  );

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedProduct) return;

    const qty = parseInt(quantity, 10);
    if (!Number.isFinite(qty) || qty <= 0) return;

    const totalPrice = selectedProduct.price * qty;
    try {
      await axios.post("/bulk-orders/", {
        product_id: parseInt(productId, 10),
        quantity: qty,
        total_price: totalPrice,
      });
      alert("Bulk order created!");
    } catch {
      alert("Failed to create bulk order.");
    }
  };

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>Create Bulk Order</h2>

        <form onSubmit={handleSubmit} className="mt-3">
          <div className="row g-3">
            <div className="col-md-6">
              <label className="form-label">Product</label>
              <select
                className="form-select"
                value={productId}
                onChange={(e) => setProductId(e.target.value)}
                required
              >
                {products.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.name} (₹{p.price})
                  </option>
                ))}
              </select>
            </div>

            <div className="col-md-3">
              <label className="form-label">Quantity</label>
              <input
                className="form-control"
                value={quantity}
                onChange={(e) => setQuantity(e.target.value)}
                type="number"
                min="1"
                required
              />
            </div>

            <div className="col-md-3 d-flex align-items-end">
              <button className="btn btn-dark w-100" type="submit">
                Place Order
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}

export default BulkOrder;