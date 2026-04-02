const API_BASE_URL = import.meta.env.VITE_API_URL;

async function apiRequest(endpoint, method = "GET", data = null) {
  const url = `${API_BASE_URL}${endpoint}`;

  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
    },
  };

  if (data) {
    options.body = JSON.stringify(data);
  }

  const response = await fetch(url, options);

  if (!response.ok) {
    throw new Error("API request failed");
  }

  return response.json();
}

const API = {
  get: (endpoint) => apiRequest(endpoint, "GET"),
  post: (endpoint, data) => apiRequest(endpoint, "POST", data),
  put: (endpoint, data) => apiRequest(endpoint, "PUT", data),
  delete: (endpoint) => apiRequest(endpoint, "DELETE"),
};

export default API;