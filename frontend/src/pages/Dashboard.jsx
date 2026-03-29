import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";
import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  ArcElement,
} from "chart.js";

ChartJS.register(
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
  ArcElement
);

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

  const barData = {
    labels: vendorData.map((v) => v.vendor_name),
    datasets: [
      {
        label: "Vendor Revenue",
        data: vendorData.map((v) => v.revenue),
      },
    ],
  };

  const pieData = {
    labels: vendorData.map((v) => v.vendor_name),
    datasets: [
      {
        data: vendorData.map((v) => v.orders),
      },
    ],
  };

  return (
    <div>
      <Navbar />

      <div className="container mt-4">
        <h2>Dashboard</h2>

        <div className="row mt-4">
          <div className="col-md-4">
            <div className="card p-3">
              <h5>Total Orders</h5>
              <h3>{data.total_orders}</h3>
            </div>
          </div>

          <div className="col-md-4">
            <div className="card p-3">
              <h5>Total Revenue</h5>
              <h3>₹{data.total_revenue}</h3>
            </div>
          </div>

          <div className="col-md-4">
            <div className="card p-3">
              <h5>Average Order Value</h5>
              <h3>₹{data.average_order_value}</h3>
            </div>
          </div>
        </div>

        <div className="card mt-4 p-3">
          <h4>Vendor Revenue Chart</h4>
          <Bar data={barData} />
        </div>

        <div className="card mt-4 p-3">
          <h4>Vendor Order Distribution</h4>
          <div style={{ width: "400px" }}>
            <Pie data={pieData} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;