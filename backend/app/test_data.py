# app/test_data.py

import requests

BASE_URL = "http://localhost:8000"

def create_vendor(name, rating):
    r = requests.post(f"{BASE_URL}/vendors", json={
        "name": name,
        "rating": rating
    })
    print("Vendor:", r.status_code, r.text)


def create_product(name, unit):
    r = requests.post(f"{BASE_URL}/products", json={
        "name": name,
        "unit": unit
    })
    print("Product:", r.status_code, r.text)


def create_vendor_product(vendor_id, product_id, price, stock, delivery_days):
    r = requests.post(f"{BASE_URL}/vendor-products", json={
        "vendor_id": vendor_id,
        "product_id": product_id,
        "price": price,
        "stock": stock,
        "delivery_days": delivery_days
    })
    print("VendorProduct:", r.status_code, r.text)


def create_bulk_order():
    r = requests.post(f"{BASE_URL}/bulk-orders", json={
        "items": [
            {"product_id": 1, "quantity": 20},
            {"product_id": 2, "quantity": 10}
        ]
    })
    print("BulkOrder:", r.status_code, r.text)


if __name__ == "__main__":
    print("\n--- Creating Test Data ---\n")

    # Vendors
    create_vendor("Vendor A", 4.5)
    create_vendor("Vendor B", 4.0)
    create_vendor("Vendor C", 4.8)

    # Products
    create_product("Rice", "kg")
    create_product("Wheat", "kg")

    # Vendor Inventory
    create_vendor_product(1, 1, 50, 100, 2)
    create_vendor_product(2, 1, 48, 100, 3)
    create_vendor_product(3, 1, 52, 100, 1)

    create_vendor_product(1, 2, 40, 100, 3)
    create_vendor_product(2, 2, 42, 100, 2)
    create_vendor_product(3, 2, 39, 100, 4)

    # Bulk Order
    create_bulk_order()

    print("\n--- Test Data Created ---\n")