import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <Link className="navbar-brand" to="/dashboard">BridgeBulks</Link>

        <div className="collapse navbar-collapse">
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/dashboard">Dashboard</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/inventory">Inventory</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/bulk-order">Bulk Order</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/comparison">Compare Vendors</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/vendor-performance-ui">Vendor Performance</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/orders">Order Status</Link>
            </li>
          </ul>

          <Link className="btn btn-outline-light" to="/login">Logout</Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;