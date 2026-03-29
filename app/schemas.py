from pydantic import BaseModel
from typing import List, Optional


# -----------------------
# Vendor
# -----------------------
class VendorCreate(BaseModel):
    name: str
    rating: float = 4.0
    delivery_time: int = 3
    reliability_score: float = 0.9


class VendorResponse(BaseModel):
    id: int
    name: str
    rating: float
    delivery_time: int
    reliability_score: float

    class Config:
        from_attributes = True


# -----------------------
# Product
# -----------------------
class ProductCreate(BaseModel):
    name: str
    unit: str


class ProductResponse(BaseModel):
    id: int
    name: str
    unit: str

    class Config:
        from_attributes = True


# -----------------------
# Vendor Product (Price Mapping)
# -----------------------
class VendorProductCreate(BaseModel):
    vendor_id: int
    product_id: int
    price: float


class VendorProductResponse(BaseModel):
    id: int
    vendor_id: int
    product_id: int
    price: float

    class Config:
        from_attributes = True


# -----------------------
# Customer
# -----------------------
class CustomerCreate(BaseModel):
    name: str
    email: str


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# -----------------------
# Bulk Order
# -----------------------
class BulkOrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class BulkOrderCreate(BaseModel):
    customer_id: int
    items: List[BulkOrderItemCreate]


class BulkOrderItemResponse(BaseModel):
    product_id: int
    quantity: int
    vendor_id: int


class BulkOrderResponse(BaseModel):
    id: int
    customer_id: int
    total_price: float
    items: List[BulkOrderItemResponse]

class CustomerRegister(BaseModel):
    name: str
    email: str
    password: str


class CustomerLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class VendorRatingCreate(BaseModel):
    order_id: int
    vendor_id: int
    rating: float
    delivery_time: int


class VendorRatingResponse(BaseModel):
    message: str