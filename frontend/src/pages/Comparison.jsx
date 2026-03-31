import { useEffect, useMemo, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function Comparison() {
  const [products, setProducts] = useState([]);
  const [productId, setProductId] = useState("");
  const [quantity, setQuantity] = useState("10");

  const [vendors, setVendors] = useState([]);
  const [selectedVendor, setSelectedVendor] = useState(null);
  const [savings, setSavings] = useState(null);

  useEffect(() => {
    axios
      .get("/products/")
      .then((res) => {
        setProducts(res.data || []);
        if (res.data && res.data.length > 0) {
          setProductId(String(res.data[0].id));
        }
      })
      .catch(() => setProducts([]));
  }, []);

  const selectedProduct = useMemo(
    () => products.find((p) => String(p.id) === String(productId)) || null,
    [products, productId]
  );

  useEffect(() => {
    const productIdInt = parseInt(productId, 10);
    const qtyInt = parseInt(quantity, 10);
    if (!Number.isFinite(productIdInt) || productIdInt <= 0) return;
    if (!Number.isFinite(qtyInt) || qtyInt <= 0) return;

    axios
      .get(`/comparison/${productIdInt}`)
      .then((res) => {
        setVendors(res.data.vendors || []);
        setSelectedVendor(res.data.selected_vendor || null);
      })
      .catch(() => {
        setVendors([]);
        setSelectedVendor(null);
      });
  }, [productId, quantity]);

  useEffect(() => {
    if (!selectedProduct || !selectedVendor) {
      setSavings(null);
      return;
    }

    const qtyInt = parseInt(quantity, 10);
    if (!Number.isFinite(qtyInt) || qtyInt <= 0) return;

    const marketPrice = selectedProduct.price * qtyInt;
    const bulkPrice = selectedVendor.price * qtyInt;

    setSavings({
      market_price: marketPrice,
      bulk_price: bulkPrice,
      savings: marketPrice - bulkPrice,
    });
  }, [selectedProduct, selectedVendor, quantity]);

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>Vendor Comparison & Savings</h2>

        <div className="row g-3 mt-2">
          <div className="col-md-6">
            <label className="form-label">Product</label>
            <select
              className="form-select"
              value={productId}
              onChange={(e) => setProductId(e.target.value)}
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
              type="number"
              min="1"
              value={quantity}
              onChange={(e) => setQuantity(e.target.value)}
            />
          </div>
        </div>

        <table className="table table-bordered mt-3">
          <thead>
            <tr>
              <th>Vendor</th>
              <th>Price</th>
              <th>Rating</th>
              <th>Delivery Days</th>
              <th>Score</th>
              <th>Selected</th>
            </tr>
          </thead>
          <tbody>
            {vendors.length === 0 ? (
              <tr>
                <td colSpan="6" className="text-center">
                  No vendor products found for this product.
                </td>
              </tr>
            ) : (
              vendors.map((v) => (
                <tr key={v.vendor_id}>
                  <td>{v.vendor_name}</td>
                  <td>₹{v.price}</td>
                  <td>{v.rating}</td>
                  <td>{v.delivery_days}</td>
                  <td>{v.score}</td>
                  <td>
                    {selectedVendor &&
                    selectedVendor.vendor_id === v.vendor_id ? (
                      <span className="badge bg-success">Selected</span>
                    ) : (
                      "-"
                    )}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>

        {savings && (
          <div className="card p-3 mt-4">
            <h4>Price Summary</h4>
            <p>Market Price: ₹{savings.market_price}</p>
            <p>Bulk Price: ₹{savings.bulk_price}</p>
            <h5 className="text-success">You Saved: ₹{savings.savings}</h5>
          </div>
        )}
      </div>
    </div>
  );
}

export default Comparison;