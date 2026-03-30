import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import CreateOrder from "./pages/CreateOrder";
import OrderHistory from "./pages/OrderHistory";
import Vendors from "./pages/Vendors";
import Comparison from "./pages/Comparison";
import OrderStatus from "./pages/OrderStatus";
import Inventory from "./pages/Inventory";
import Profile from "./pages/Profile";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/create-order" element={<CreateOrder />} />
        <Route path="/orders" element={<OrderHistory />} />
        <Route path="/vendors" element={<Vendors />} />
        <Route path="/comparison" element={<Comparison />} />
        <Route path="/order-status" element={<OrderStatus />} />
        <Route path="/inventory" element={<Inventory/>}/>
        <Route path="profile" element={<Profile/>}/>
      </Routes>
    </Router>
  );
}

export default App;