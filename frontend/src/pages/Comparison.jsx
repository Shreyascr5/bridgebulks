import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function Comparison() {
  const [vendors, setVendors] = useState([]);
  const [selectedVendor, setSelectedVendor] = useState(null);
  const [savings, setSavings] = useState(null);

  const productId = 1; // demo
  const orderId = 1;   // demo

  useEffect(() => {
    fetchComparison();
    fetchSavings();
  }, []);

  const fetchComparison = async () => {
    const res = await axios.get(`http://127.0.0.1:8000/comparison/${productId}`);
    setVendors(res.data.vendors);
    setSelectedVendor(res.data.selected_vendor);
  };

  const fetchSavings = async () => {
    const res = await axios.get(`http://127.0.0.1:8000/bulk-orders/${orderId}/savings`);
    setSavings(res.data);
  };

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>Vendor Comparison & Savings</h2>

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
            {vendors.map((v) => (
              <tr key={v.vendor_id}>
                <td>{v.vendor_name}</td>
                <td>₹{v.price}</td>
                <td>{v.rating}</td>
                <td>{v.delivery_days}</td>
                <td>{v.score}</td>
                <td>
                  {selectedVendor && selectedVendor.vendor_id === v.vendor_id ? (
                    <span className="badge bg-success">Selected</span>
                  ) : (
                    "-"
                  )}
                </td>
              </tr>
            ))}
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