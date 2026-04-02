import React from "react";
import ReactDOM from "react-dom/client";
import { HashRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Vendors from "./pages/Vendors";
import Inventory from "./pages/Inventory";
import BulkOrder from "./pages/BulkOrder";
import Comparison from "./pages/Comparison";
import OrderHistory from "./pages/OrderHistory";
import OrderStatus from "./pages/OrderStatus";
import Profile from "./pages/Profile";

ReactDOM.createRoot(document.getElementById("root")).render(
  <HashRouter>
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/vendors" element={<Vendors />} />
      <Route path="/inventory" element={<Inventory />} />
      <Route path="/bulk-order" element={<BulkOrder />} />
      <Route path="/comparison" element={<Comparison />} />
      <Route path="/order-history" element={<OrderHistory />} />
      <Route path="/order-status" element={<OrderStatus />} />
      <Route path="/profile" element={<Profile />} />
    </Routes>
  </HashRouter>
);