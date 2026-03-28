from pydantic import BaseModel
from typing import List


# --------------------
# VENDOR
# --------------------
class VendorCreate(BaseModel):
    name: str

class VendorResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# --------------------
# PRODUCT
# --------------------
class ProductCreate(BaseModel):
    name: str
    unit: str

class ProductResponse(BaseModel):
    id: int
    name: str
    unit: str

    class Config:
        from_attributes = True


# --------------------
# CUSTOMER
# --------------------
class CustomerCreate(BaseModel):
    name: str
    email: str

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# --------------------
# VENDOR PRODUCT PRICING
# --------------------
class VendorProductCreate(BaseModel):
    vendor_id: int
    product_id: int
    price: float


# --------------------
# BULK ORDER
# --------------------
class BulkOrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class BulkOrderCreate(BaseModel):
    customer_id: int
    items: List[BulkOrderItemCreate]