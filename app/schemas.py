from pydantic import BaseModel
from typing import List, Optional

class VendorCreate(BaseModel):
    name: str

class VendorResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    unit: str

class ProductResponse(BaseModel):
    id: int
    name: str
    unit: str

    class Config:
        from_attributes = True

class VendorProductCreate(BaseModel):
    vendor_id: int
    product_id: int
    price: float

class BulkOrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class BulkOrderCreate(BaseModel):
    items: List[BulkOrderItemCreate]

class BulkOrderItemResponse(BaseModel):
    product_id: int
    quantity: int
    vendor_id: int

    class Config:
        from_attributes = True

class BulkOrderResponse(BaseModel):
    id: int
    vendor_id: Optional[int]
    total_price: float
    items: List[BulkOrderItemResponse]

    class Config:
        from_attributes = True