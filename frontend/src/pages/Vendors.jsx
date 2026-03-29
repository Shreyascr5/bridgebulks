import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function Vendors() {
  const [vendors, setVendors] = useState([]);

  useEffect(() => {
    const fetchVendors = async () => {
      const res = await axios.get("http://127.0.0.1:8000/vendor-performance/");
      setVendors(res.data);
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
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>Vendor Performance</h2>

        {vendors.map((v, index) => (
          <div className="card p-3 mt-3" key={index}>
            <h5>{v.vendor}</h5>
            <p>Average Rating: {v.avg_rating} {renderStars(v.avg_rating)}</p>
            <p>Avg Delivery Time: {v.avg_delivery} days</p>
            <p>Total Orders: {v.total_orders}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Vendors;