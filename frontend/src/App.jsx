import { Routes, Route, useLocation } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import BulkOrder from "./pages/BulkOrder";
import Inventory from "./pages/Inventory";
import Comparison from "./pages/Comparison";
import Vendors from "./pages/Vendors";
import OrderHistory from "./pages/OrderHistory";
import OrderStatus from "./pages/OrderStatus";
import Profile from "./pages/Profile";
import Navbar from "./components/Navbar";

// Pages where Navbar should be hidden
const AUTH_PAGES = ["/", "/login", "/register"];

function App() {
  const location = useLocation();
  const showNavbar = !AUTH_PAGES.includes(location.pathname);

  return (
    <div>
      {showNavbar && <Navbar />}
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/bulk-order" element={<BulkOrder />} />
        <Route path="/inventory" element={<Inventory />} />
        <Route path="/comparison" element={<Comparison />} />
        <Route path="/vendor-performance-ui" element={<Vendors />} />
        <Route path="/orders" element={<OrderHistory />} />
        <Route path="/order-status" element={<OrderStatus />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </div>
  );
}

export default App;