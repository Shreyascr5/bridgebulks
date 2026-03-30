import { useEffect, useState } from "react";
import API from "../api";
import Navbar from "../components/Navbar";

function Inventory() {
  const [inventory, setInventory] = useState([]);
  const [form, setForm] = useState({
    vendor_id: "",
    product_id: "",
    price: "",
    stock: "",
    delivery_days: "",
  });

  useEffect(() => {
    fetchInventory();
  }, []);

  const fetchInventory = async () => {
    const res = await API.get("/inventory/");
    setInventory(res.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await API.post("/inventory/", form);
    fetchInventory();
  };

  return (
    <div>
      <Navbar />
      <div className="container mt-4">
        <h2>Vendor Inventory</h2>

        <form onSubmit={handleSubmit} className="mb-4">
          <input className="form-control mb-2" placeholder="Vendor ID"
            onChange={(e) => setForm({...form, vendor_id: e.target.value})}/>
          <input className="form-control mb-2" placeholder="Product ID"
            onChange={(e) => setForm({...form, product_id: e.target.value})}/>
          <input className="form-control mb-2" placeholder="Price"
            onChange={(e) => setForm({...form, price: e.target.value})}/>
          <input className="form-control mb-2" placeholder="Stock"
            onChange={(e) => setForm({...form, stock: e.target.value})}/>
          <input className="form-control mb-2" placeholder="Delivery Days"
            onChange={(e) => setForm({...form, delivery_days: e.target.value})}/>
          <button className="btn btn-primary">Add Inventory</button>
        </form>

        <table className="table table-bordered">
          <thead>
            <tr>
              <th>Vendor</th>
              <th>Product</th>
              <th>Price</th>
              <th>Stock</th>
              <th>Delivery</th>
            </tr>
          </thead>
          <tbody>
            {inventory.map((i) => (
              <tr key={i.id}>
                <td>{i.vendor_id}</td>
                <td>{i.product_id}</td>
                <td>{i.price}</td>
                <td>{i.stock}</td>
                <td>{i.delivery_days}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Inventory;