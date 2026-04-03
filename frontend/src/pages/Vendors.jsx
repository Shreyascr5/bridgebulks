import { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function Vendors() {
  const [vendors, setVendors] = useState([]);

  useEffect(() => {
    const fetchVendors = async () => {
      try {
        const res = await axios.get(`${API_BASE_URL}/vendor-performance/`);
        setVendors(res.data || []);
      } catch {
        setVendors([]);
      }
    };

    fetchVendors();
  }, []);

  const renderStars = (rating) => {
    let stars = "";
    for (let i = 0; i < Math.round(rating); i++) {
      stars += "⭐";
    }
    return stars;
  };

  return (
    <div className="container mt-4">
      <h2>Vendor Performance</h2>

      {vendors.length === 0 ? (
        <div className="alert alert-info mt-3">No vendor performance data yet.</div>
      ) : (
        vendors.map((v, index) => (
          <div className="card p-3 mt-3" key={index}>
            <h5>{v.vendor}</h5>
            <p>
              Average Rating: {v.avg_rating} {renderStars(v.avg_rating)}
            </p>
            <p>Avg Delivery Time: {v.avg_delivery} days</p>
            <p>Total Orders: {v.total_orders}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default Vendors;