const API = {
  register: (data) =>
    fetch("/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    }),

  login: (data) =>
    fetch("/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    }),

  createVendor: (data) =>
    fetch("/vendors/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    }),

  createProduct: (data) =>
    fetch("/products/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    }),

  createOrder: (data) =>
    fetch("/bulk-orders/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    }),

  getDashboard: () =>
    fetch("/analytics/dashboard").then((res) => res.json()),
};

export default API;