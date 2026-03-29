import { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

function Dashboard() {
  const [data, setData] = useState({});
  const [vendorData, setVendorData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await axios.get("http://127.0.0.1:8000/analytics");
      setData(res.data);
      setVendorData(res.data.vendor_stats);
    };
    fetchData();
  }, []);

  const chartData = {
    labels: vendorData.map((v) => v.vendor_name),
    datasets: [
      {
        label: "Vendor Revenue",
        data: vendorData.map((v) => v.revenue),
      },
    ],
  };

  return (
    <div>
      <h2>BridgeBulks Dashboard</h2>

      <button onClick={() => (window.location.href = "/create-order")}>
        Create Order
      </button>
      <button onClick={() => (window.location.href = "/orders")}>
        Order History
      </button>
      <button onClick={() => (window.location.href = "/vendors")}>
        Vendor Performance
      </button>

      <h3>Analytics</h3>
      <p>Total Orders: {data.total_orders}</p>
      <p>Total Revenue: {data.total_revenue}</p>
      <p>Average Order Value: {data.average_order_value}</p>

      <h3>Vendor Revenue Chart</h3>
      <div style={{ width: "500px" }}>
        <Bar data={chartData} />
      </div>
    </div>
  );
}

export default Dashboard;