from pydantic import BaseModel
from typing import List

# ---------- Vendor ----------
class VendorCreate(BaseModel):
    name: str

class VendorResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# ---------- Product ----------
class ProductCreate(BaseModel):
    name: str
    unit: str

class ProductResponse(BaseModel):
    id: int
    name: str
    unit: str

    class Config:
        from_attributes = True


# ---------- Bulk Order ----------
class BulkOrderItemCreate(BaseModel):
    product_id: int
    quantity: float


class BulkOrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    quantity: float

    class Config:
        from_attributes = True


class BulkOrderCreate(BaseModel):
    vendor_id: int
    items: List[BulkOrderItemCreate]


class BulkOrderResponse(BaseModel):
    id: int
    vendor_id: int
    items: List[BulkOrderItemResponse]
