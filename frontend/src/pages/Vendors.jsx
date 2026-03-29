import { useEffect, useState } from "react";
import axios from "axios";

function Vendors() {
  const [vendors, setVendors] = useState([]);

  useEffect(() => {
    const fetchVendors = async () => {
      const res = await axios.get("http://127.0.0.1:8000/analytics");
      setVendors(res.data.vendor_stats);
    };

    fetchVendors();
  }, []);

  return (
    <div>
      <h2>Vendor Performance</h2>

      {vendors.map((v, index) => (
        <div key={index}>
          <p>Name: {v.vendor_name}</p>
          <p>Revenue: {v.revenue}</p>
          <p>Orders: {v.orders}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default Vendors;