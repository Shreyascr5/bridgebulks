from pydantic import BaseModel
from typing import List, Optional

# --------------------
# Vendor Schemas
# --------------------
class VendorCreate(BaseModel):
    name: str
    location: Optional[str] = None


class VendorResponse(VendorCreate):
    id: int

    class Config:
        from_attributes = True


# --------------------
# Product Schemas
# --------------------
class ProductCreate(BaseModel):
    name: str
    price: int
    vendor_id: int


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True


# --------------------
# Bulk Order Item Schemas
# --------------------
class BulkOrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class BulkOrderItemResponse(BulkOrderItemCreate):
    id: int

    class Config:
        from_attributes = True


# --------------------
# Bulk Order Schemas
# --------------------
class BulkOrderCreate(BaseModel):
    vendor_id: int
    items: List[BulkOrderItemCreate]


class BulkOrderResponse(BaseModel):
    id: int
    vendor_id: int
    status: str
    items: List[BulkOrderItemResponse]

    class Config:
        from_attributes = True
