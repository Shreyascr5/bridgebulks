import { useEffect, useState } from "react";
import API from "../api";
import Navbar from "../components/Navbar";

function Dashboard() {
  const [data, setData] = useState({
    total_orders: 0,
    total_revenue: 0,
    average_order_value: 0,
  });

  useEffect(() => {
    API.getDashboard().then((res) => setData(res));
  }, []);

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
      </div>
    </div>
  );
}

export default Dashboard;