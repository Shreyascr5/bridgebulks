// Read the backend URL from the Vite env variable set in Render dashboard.
// Falls back to localhost for local development.
const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://localhost:8000";

async function apiRequest(endpoint, method = "GET", data = null) {
  const url = `${API_BASE_URL}${endpoint}`;

  const headers = { "Content-Type": "application/json" };

  // Attach JWT token when present
  const token = localStorage.getItem("token");
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const options = { method, headers };
  if (data) {
    options.body = JSON.stringify(data);
  }

  const response = await fetch(url, options);

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`API ${method} ${endpoint} failed (${response.status}): ${errorText}`);
  }

  return response.json();
}

const API = {
  // Generic helpers
  get:    (endpoint)       => apiRequest(endpoint, "GET"),
  post:   (endpoint, data) => apiRequest(endpoint, "POST",   data),
  put:    (endpoint, data) => apiRequest(endpoint, "PUT",    data),
  delete: (endpoint)       => apiRequest(endpoint, "DELETE"),

  // Named methods used by page components
  getDashboard:        () => apiRequest("/analytics/dashboard",        "GET"),
  getRevenueByProduct: () => apiRequest("/analytics/revenue-by-product","GET"),
  getOrdersByProduct:  () => apiRequest("/analytics/orders-by-product", "GET"),
};

export default API;