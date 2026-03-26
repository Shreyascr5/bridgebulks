from pydantic import BaseModel
from typing import List

# -------- Vendor --------
class VendorCreate(BaseModel):
    name: str
    rating: float
    distance: float

class VendorResponse(BaseModel):
    id: int
    name: str
    rating: float
    distance: float

    class Config:
        from_attributes = True


# -------- Product --------
class ProductCreate(BaseModel):
    name: str
    unit: str

class ProductResponse(BaseModel):
    id: int
    name: str
    unit: str

    class Config:
        from_attributes = True


# -------- Vendor Product Pricing --------
class VendorProductCreate(BaseModel):
    vendor_id: int
    product_id: int
    price: float


# -------- Bulk Order --------
class BulkOrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class BulkOrderCreate(BaseModel):
    items: List[BulkOrderItemCreate]

class BulkOrderItemResponse(BaseModel):
    product_id: int
    quantity: int
    vendor_id: int
    price: float
    rating: float
    distance: float
    score: float

    class Config:
        from_attributes = True

class BulkOrderResponse(BaseModel):
    id: int
    total_price: float
    items: List[BulkOrderItemResponse]

    class Config:
        from_attributes = True