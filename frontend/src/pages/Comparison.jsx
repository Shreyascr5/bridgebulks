import { useEffect, useMemo, useState } from "react";
import axios from "axios";

function Comparison() {
  const [products, setProducts] = useState([]);
  const [productId, setProductId] = useState("");

  const [vendors, setVendors] = useState([]);
  const [selectedVendor, setSelectedVendor] = useState(null);

  // Multi-buyer consortium: each buyer contributes a quantity.
  // Savings are split proportionally to each buyer's quantity.
  const [buyers, setBuyers] = useState([
    { id: 1, name: "Buyer A", qty: "2" },
    { id: 2, name: "Buyer B", qty: "3" },
    { id: 3, name: "Buyer C", qty: "1" },
  ]);

  useEffect(() => {
    axios
      .get("/products/")
      .then((res) => {
        setProducts(res.data || []);
        if (res.data && res.data.length > 0) {
          setProductId(String(res.data[0].id));
        }
      })
      .catch(() => setProducts([]));
  }, []);

  const selectedProduct = useMemo(
    () => products.find((p) => String(p.id) === String(productId)) || null,
    [products, productId]
  );

  useEffect(() => {
    const productIdInt = parseInt(productId, 10);
    if (!Number.isFinite(productIdInt) || productIdInt <= 0) return;

    axios
      .get(`/comparison/${productIdInt}`)
      .then((res) => {
        setVendors(res.data.vendors || []);
        setSelectedVendor(res.data.selected_vendor || null);
      })
      .catch(() => {
        setVendors([]);
        setSelectedVendor(null);
      });
  }, [productId]);

  const parsedBuyers = useMemo(() => {
    return buyers
      .map((b) => {
        const qtyInt = parseInt(b.qty, 10);
        return {
          ...b,
          qtyInt: Number.isFinite(qtyInt) && qtyInt > 0 ? qtyInt : 0,
        };
      })
      .filter((b) => b.name.trim().length > 0);
  }, [buyers]);

  const totalQty = useMemo(
    () => parsedBuyers.reduce((sum, b) => sum + b.qtyInt, 0),
    [parsedBuyers]
  );

  const consortiumTotals = useMemo(() => {
    if (!selectedProduct || !selectedVendor) return null;
    if (totalQty <= 0) return null;

    const marketPriceTotal = selectedProduct.price * totalQty;
    const bulkPriceTotal = selectedVendor.price * totalQty;
    const savingsTotal = marketPriceTotal - bulkPriceTotal;

    return {
      marketPriceTotal,
      bulkPriceTotal,
      savingsTotal,
    };
  }, [selectedProduct, selectedVendor, totalQty]);

  const buyerAllocations = useMemo(() => {
    if (!consortiumTotals || !selectedProduct || !selectedVendor) return [];
    if (totalQty <= 0) return [];

    return parsedBuyers
      .map((b) => {
        if (b.qtyInt <= 0) return null;

        const buyerMarket = selectedProduct.price * b.qtyInt;
        const buyerBulk = selectedVendor.price * b.qtyInt;
        const buyerSavings = buyerMarket - buyerBulk;
        const savingsShare =
          consortiumTotals.savingsTotal !== 0
            ? buyerSavings / consortiumTotals.savingsTotal
            : 0;

        return {
          ...b,
          buyerMarket,
          buyerBulk,
          buyerSavings,
          savingsShare,
        };
      })
      .filter(Boolean);
  }, [
    parsedBuyers,
    consortiumTotals,
    selectedProduct,
    selectedVendor,
    totalQty,
  ]);

  const addBuyer = () => {
    setBuyers((prev) => {
      const nextId = prev.length ? Math.max(...prev.map((b) => b.id)) + 1 : 1;
      return [...prev, { id: nextId, name: `Buyer ${nextId}`, qty: "1" }];
    });
  };

  const removeBuyer = (id) => {
    setBuyers((prev) => prev.filter((b) => b.id !== id));
  };

  const createConsortiumOrder = async () => {
    if (!selectedProduct || !selectedVendor) return;
    if (totalQty <= 0) return;

    const payload = {
      product_id: parseInt(productId, 10),
      quantity: totalQty,
      total_price: consortiumTotals ? consortiumTotals.bulkPriceTotal : 0,
    };

    try {
      await axios.post("/bulk-orders/", payload);
      alert("Consortium bulk order created!");
    } catch {
      alert("Failed to create consortium bulk order.");
    }
  };

  return (
    <div className="container mt-4">
      <h2>Vendor Comparison & Consortium Savings</h2>

      <div className="row g-3 mt-2">
        <div className="col-md-6">
          <label className="form-label">Product</label>
          <select
            className="form-select"
            value={productId}
            onChange={(e) => setProductId(e.target.value)}
          >
            {products.map((p) => (
              <option key={p.id} value={p.id}>
                {p.name} (₹{p.price})
              </option>
            ))}
          </select>
        </div>

        <div className="col-md-6">
          <label className="form-label">Consortium Buyers</label>
          <div className="card p-3">
            <div className="d-flex justify-content-between align-items-center">
              <div>
                <div className="fw-semibold">Total Qty: {totalQty}</div>
                <div className="text-muted" style={{ fontSize: 13 }}>
                  Savings split is proportional to quantity.
                </div>
              </div>
              <button className="btn btn-sm btn-outline-dark" onClick={addBuyer} type="button">
                + Add Buyer
              </button>
            </div>

            <div className="table-responsive mt-3">
              <table className="table table-sm table-bordered align-middle">
                <thead>
                  <tr>
                    <th>Buyer</th>
                    <th style={{ width: 110 }}>Qty</th>
                    <th style={{ width: 80 }}></th>
                  </tr>
                </thead>
                <tbody>
                  {buyers.map((b) => (
                    <tr key={b.id}>
                      <td>
                        <input
                          className="form-control form-control-sm"
                          value={b.name}
                          onChange={(e) =>
                            setBuyers((prev) =>
                              prev.map((x) =>
                                x.id === b.id ? { ...x, name: e.target.value } : x
                              )
                            )
                          }
                        />
                      </td>
                      <td>
                        <input
                          className="form-control form-control-sm"
                          type="number"
                          min="0"
                          value={b.qty}
                          onChange={(e) =>
                            setBuyers((prev) =>
                              prev.map((x) =>
                                x.id === b.id ? { ...x, qty: e.target.value } : x
                              )
                            )
                          }
                        />
                      </td>
                      <td>
                        <button
                          className="btn btn-sm btn-outline-danger"
                          type="button"
                          onClick={() => removeBuyer(b.id)}
                          disabled={buyers.length <= 1}
                        >
                          Remove
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <table className="table table-bordered mt-4">
        <thead>
          <tr>
            <th>Vendor</th>
            <th>Price</th>
            <th>Rating</th>
            <th>Delivery Days</th>
            <th>Score</th>
            <th>Selected</th>
          </tr>
        </thead>
        <tbody>
          {vendors.length === 0 ? (
            <tr>
              <td colSpan="6" className="text-center">
                No vendor products found for this product.
              </td>
            </tr>
          ) : (
            vendors.map((v) => (
              <tr key={v.vendor_id}>
                <td>{v.vendor_name}</td>
                <td>₹{v.price}</td>
                <td>{v.rating}</td>
                <td>{v.delivery_days}</td>
                <td>{v.score}</td>
                <td>
                  {selectedVendor &&
                  selectedVendor.vendor_id === v.vendor_id ? (
                    <span className="badge bg-success">Selected</span>
                  ) : (
                    "-"
                  )}
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>

      {consortiumTotals && (
        <div className="card p-3 mt-4">
          <h4>Consortium Price Summary</h4>
          <p className="mb-1">Market Price (if bought separately): ₹{consortiumTotals.marketPriceTotal}</p>
          <p className="mb-1">Consortium Bulk Price: ₹{consortiumTotals.bulkPriceTotal}</p>
          <h5 className="text-success mb-3">Total Savings: ₹{consortiumTotals.savingsTotal}</h5>

          <div className="table-responsive">
            <table className="table table-bordered">
              <thead>
                <tr>
                  <th>Buyer</th>
                  <th>Qty</th>
                  <th>Market Price</th>
                  <th>Bulk Price</th>
                  <th>Allocated Savings</th>
                  <th>% Share</th>
                </tr>
              </thead>
              <tbody>
                {buyerAllocations.length === 0 ? (
                  <tr>
                    <td colSpan="6" className="text-center">
                      Enter quantities above to see the split.
                    </td>
                  </tr>
                ) : (
                  buyerAllocations.map((b) => (
                    <tr key={b.id}>
                      <td>{b.name}</td>
                      <td>{b.qtyInt}</td>
                      <td>₹{b.buyerMarket}</td>
                      <td>₹{b.buyerBulk}</td>
                      <td className="text-success">₹{b.buyerSavings}</td>
                      <td>
                        {consortiumTotals.savingsTotal !== 0
                          ? `${Math.round(b.savingsShare * 100)}%`
                          : "0%"}
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>

          <div className="d-flex justify-content-end mt-3">
            <button
              className="btn btn-dark"
              onClick={createConsortiumOrder}
              disabled={!selectedVendor || totalQty <= 0}
              type="button"
            >
              Create Consortium Bulk Order
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Comparison;