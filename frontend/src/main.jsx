import React from "react";
import ReactDOM from "react-dom/client";
import { HashRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Vendors from "./pages/Vendors";
import Products from "./pages/Products";
import BulkOrders from "./pages/BulkOrders";
import Analytics from "./pages/Analytics";

ReactDOM.createRoot(document.getElementById("root")).render(
  <HashRouter>
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/vendors" element={<Vendors />} />
      <Route path="/products" element={<Products />} />
      <Route path="/bulk-orders" element={<BulkOrders />} />
      <Route path="/analytics" element={<Analytics />} />
    </Routes>
  </HashRouter>
);