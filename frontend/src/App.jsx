import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import BulkOrder from "./pages/BulkOrder";
import Inventory from "./pages/Inventory";
import Comparison from "./pages/Comparison";
import Vendors from "./pages/Vendors";
import OrderHistory from "./pages/OrderHistory";
import Navbar from "./components/Navbar";

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/bulk-order" element={<BulkOrder />} />
          <Route path="/bulk-order/" element={<BulkOrder />} />
          <Route path="/inventory" element={<Inventory />} />
          <Route path="/inventory/" element={<Inventory />} />
          <Route path="/comparison" element={<Comparison />} />
          <Route path="/comparison/" element={<Comparison />} />
          <Route path="/vendor-performance-ui" element={<Vendors />} />
          <Route path="/vendor-performance-ui/" element={<Vendors />} />
          <Route path="/orders" element={<OrderHistory />} />
          <Route path="/orders/" element={<OrderHistory />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;