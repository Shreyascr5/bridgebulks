import requests

BASE_URL = "http://127.0.0.1:8000"


def print_response(r):
    print("Status:", r.status_code)
    try:
        print("Response:", r.json())
    except:
        print("Raw Response:", r.text)
    print("-" * 50)


def test_create_vendor():
    data = {"name": "Vendor A"}
    r = requests.post(f"{BASE_URL}/vendors/", json=data)
    print("Create Vendor")
    print_response(r)


def test_create_product():
    data = {"name": "Rice", "unit": "kg"}
    r = requests.post(f"{BASE_URL}/products/", json=data)
    print("Create Product")
    print_response(r)


def test_vendor_product():
    data = {
        "vendor_id": 1,
        "product_id": 1,
        "price": 50
    }
    r = requests.post(f"{BASE_URL}/vendor-products/", json=data)
    print("Vendor Product")
    print_response(r)


def test_create_customer():
    data = {
        "name": "Customer A",
        "email": "customer@test.com"
    }
    r = requests.post(f"{BASE_URL}/customers/", json=data)
    print("Create Customer")
    print_response(r)


def test_bulk_order():
    data = {
        "customer_id": 1,
        "items": [
            {"product_id": 1, "quantity": 10}
        ]
    }
    r = requests.post(f"{BASE_URL}/bulk-orders/", json=data)
    print("Bulk Order")
    print_response(r)


if __name__ == "__main__":
    test_create_vendor()
    test_create_product()
    test_vendor_product()
    test_create_customer()
    test_bulk_order()