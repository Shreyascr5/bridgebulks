from pydantic import BaseModel
from typing import List, Optional

# ---------------- VENDORS ----------------
class VendorCreate(BaseModel):
    name: str
    location: Optional[str] = None

class VendorResponse(VendorCreate):
    id: int

    class Config:
        from_attributes = True


# ---------------- PRODUCTS ----------------
class ProductCreate(BaseModel):
    name: str
    price: int
    vendor_id: int

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True


# ---------------- CUSTOMERS ----------------
class CustomerCreate(BaseModel):
    name: str
    phone: str

class CustomerResponse(CustomerCreate):
    id: int

    class Config:
        from_attributes = True


# ---------------- ORDERS ----------------
class OrderCreate(BaseModel):
    product_name: str
    quantity: int

class OrderResponse(OrderCreate):
    id: int
    customer_id: int

    class Config:
        from_attributes = True


# ---------------- BULK ORDERS (SAFE PLACEHOLDER) ----------------
class BulkOrderCreate(BaseModel):
    vendor_id: int
    total_quantity: int

class BulkOrderResponse(BulkOrderCreate):
    id: int

    class Config:
        from_attributes = True
