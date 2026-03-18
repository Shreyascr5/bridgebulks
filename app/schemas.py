from pydantic import BaseModel
from typing import List, Optional

# -----------------------
# VENDOR
# -----------------------

class VendorCreate(BaseModel):
    name: str

class VendorResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# -----------------------
# PRODUCT
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
# VENDOR PRODUCT (PRICING)
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
# BULK ORDER ITEMS
# -----------------------

class BulkOrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class BulkOrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True


# -----------------------
# BULK ORDER
# -----------------------

class BulkOrderCreate(BaseModel):
    items: List[BulkOrderItemCreate]

class BulkOrderResponse(BaseModel):
    id: int
    vendor_id: int
    total_price: Optional[float]
    items: List[BulkOrderItemResponse]

    class Config:
        from_attributes = True