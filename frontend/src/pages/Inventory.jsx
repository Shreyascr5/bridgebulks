import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";

function Inventory() {
  const [vendors, setVendors] = useState([]);
  const [products, setProducts] = useState([]);
  const [inventory, setInventory] = useState([]);

  const [vendorId, setVendorId] = useState("");
  const [productId, setProductId] = useState("");
  const [price, setPrice] = useState("");
  const [stock, setStock] = useState("");
  const [deliveryDays, setDeliveryDays] = useState("");

  useEffect(() => {
    loadData();
  }, []);

  const loadData = () => {
    fetch("/vendors/").then(res => res.json()).then(setVendors);
    fetch("/products/").then(res => res.json()).then(setProducts);
    fetch("/vendor-products/").then(res => res.json()).then(setInventory);
  };

  const getVendorName = (id) => {
    const v = vendors.find(v => v.id === id);
    return v ? v.name : id;
  };

  const getProductName = (id) => {
    const p = products.find(p => p.id === id);
    return p ? p.name : id;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      vendor_id: parseInt(vendorId),
      product_id: parseInt(productId),
      price: parseFloat(price),
      stock: parseInt(stock),
      delivery_days: parseInt(deliveryDays),
    };

    await fetch("/vendor-products/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    alert("Inventory Added");
    loadData();
  };

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>Inventory Management</h2>

        <form onSubmit={handleSubmit} className="mb-4">
          <div className="row">
            <div className="col">
              <select className="form-control" onChange={(e) => setVendorId(e.target.value)}>
                <option>Select Vendor</option>
                {vendors.map(v => (
                  <option key={v.id} value={v.id}>{v.name}</option>
                ))}
              </select>
            </div>

            <div className="col">
              <select className="form-control" onChange={(e) => setProductId(e.target.value)}>
                <option>Select Product</option>
                {products.map(p => (
                  <option key={p.id} value={p.id}>{p.name}</option>
                ))}
              </select>
            </div>

            <div className="col">
              <input className="form-control" placeholder="Price" onChange={(e) => setPrice(e.target.value)} />
            </div>

            <div className="col">
              <input className="form-control" placeholder="Stock" onChange={(e) => setStock(e.target.value)} />
            </div>

            <div className="col">
              <input className="form-control" placeholder="Delivery Days" onChange={(e) => setDeliveryDays(e.target.value)} />
            </div>

            <div className="col">
              <button className="btn btn-primary">Add</button>
            </div>
          </div>
        </form>

        <table className="table table-striped">
          <thead>
            <tr>
              <th>Vendor</th>
              <th>Product</th>
              <th>Price</th>
              <th>Stock</th>
              <th>Delivery Days</th>
            </tr>
          </thead>
          <tbody>
            {inventory.map(item => (
              <tr key={item.id}>
                <td>{getVendorName(item.vendor_id)}</td>
                <td>{getProductName(item.product_id)}</td>
                <td>{item.price}</td>
                <td>{item.stock}</td>
                <td>{item.delivery_days}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Inventory;