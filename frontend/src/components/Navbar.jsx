function Navbar() {
  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  return (
    <nav className="navbar navbar-dark bg-dark navbar-expand-lg">
      <div className="container-fluid">
        <a className="navbar-brand" href="/dashboard">
          BridgeBulks
        </a>

        <div>
          <a className="btn btn-outline-light me-2" href="/dashboard">
            Dashboard
          </a>
          <a className="btn btn-outline-light me-2" href="/create-order">
            Create Order
          </a>
          <a className="btn btn-outline-light me-2" href="/orders">
            Orders
          </a>
          <a className="btn btn-outline-light me-2" href="/vendors">
            Vendors
          </a>
          <a className="btn btn-outline-light me-2" href="/profile">
            Profile
          </a>
          <button className="btn btn-danger" onClick={logout}>
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
