import { useEffect, useState } from "react";
import API from "../api";
import Navbar from "../components/Navbar";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from "chart.js";
import { Bar, Doughnut } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement
);

function Dashboard() {
  const [data, setData] = useState({
    total_orders: 0,
    total_revenue: 0,
    average_order_value: 0,
  });

  const [revenueByProduct, setRevenueByProduct] = useState([]);
  const [ordersByProduct, setOrdersByProduct] = useState([]);

  useEffect(() => {
    API.getDashboard()
      .then((res) => setData(res))
      .catch(() => setData({ total_orders: 0, total_revenue: 0, average_order_value: 0 }));
    API.getRevenueByProduct()
      .then((res) => setRevenueByProduct(res || []))
      .catch(() => setRevenueByProduct([]));
    API.getOrdersByProduct()
      .then((res) => setOrdersByProduct(res || []))
      .catch(() => setOrdersByProduct([]));
  }, []);

  const revenueChart = {
    labels: revenueByProduct.map((r) => r.product_name),
    datasets: [
      {
        label: "Revenue",
        data: revenueByProduct.map((r) => r.revenue),
        backgroundColor: "rgba(13, 110, 253, 0.5)",
      },
    ],
  };

  const ordersChart = {
    labels: ordersByProduct.map((r) => r.product_name),
    datasets: [
      {
        label: "Orders",
        data: ordersByProduct.map((r) => r.orders),
        backgroundColor: [
          "rgba(25, 135, 84, 0.6)",
          "rgba(13, 110, 253, 0.6)",
          "rgba(255, 193, 7, 0.6)",
          "rgba(220, 53, 69, 0.6)",
          "rgba(108, 117, 125, 0.6)",
        ],
      },
    ],
  };

  return (
    <div>
      <Navbar />

      <div className="container mt-4">
        <h2 className="mb-4">Analytics Dashboard</h2>

        <div className="row">
          <div className="col-md-4">
            <div className="card text-center shadow">
              <div className="card-body">
                <h5>Total Orders</h5>
                <h3>{data.total_orders}</h3>
              </div>
            </div>
          </div>

          <div className="col-md-4">
            <div className="card text-center shadow">
              <div className="card-body">
                <h5>Total Revenue</h5>
                <h3>₹ {data.total_revenue}</h3>
              </div>
            </div>
          </div>

          <div className="col-md-4">
            <div className="card text-center shadow">
              <div className="card-body">
                <h5>Avg Order Value</h5>
                <h3>₹ {data.average_order_value}</h3>
              </div>
            </div>
          </div>
        </div>

        <div className="row mt-4">
          <div className="col-md-8">
            <div className="card p-3 shadow">
              <h4>Revenue by Product</h4>
              <Bar
                data={revenueChart}
                options={{
                  responsive: true,
                  plugins: {
                    legend: { display: true },
                  },
                }}
              />
            </div>
          </div>

          <div className="col-md-4">
            <div className="card p-3 shadow">
              <h4>Orders by Product</h4>
              <Doughnut
                data={ordersChart}
                options={{
                  responsive: true,
                  plugins: {
                    legend: { position: "bottom" },
                  },
                }}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;