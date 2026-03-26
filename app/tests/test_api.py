import requests

BASE_URL = "http://127.0.0.1:8000"

def test_create_vendor():
    data = {
        "name": "Test Vendor",
        "rating": 4.2,
        "distance": 12
    }
    response = requests.post(f"{BASE_URL}/vendors/", json=data)
    print("Create Vendor:", response.json())

def test_create_product():
    data = {
        "name": "Test Product",
        "unit": "kg"
    }
    response = requests.post(f"{BASE_URL}/products/", json=data)
    print("Create Product:", response.json())

def test_vendor_pricing():
    data = {
        "vendor_id": 1,
        "product_id": 1,
        "price": 55
    }
    response = requests.post(f"{BASE_URL}/vendor-products/", json=data)
    print("Vendor Pricing:", response.json())

def test_bulk_order():
    data = {
        "items": [
            {"product_id": 1, "quantity": 10},
            {"product_id": 2, "quantity": 5}
        ]
    }
    response = requests.post(f"{BASE_URL}/bulk-orders/", json=data)
    print("Bulk Order:", response.json())

def test_analytics():
    response = requests.get(f"{BASE_URL}/analytics/")
    print("Analytics:", response.json())

if __name__ == "__main__":
    test_create_vendor()
    test_create_product()
    test_vendor_pricing()
    test_bulk_order()
    test_analytics()