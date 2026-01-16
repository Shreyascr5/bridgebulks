from pydantic import BaseModel
from typing import List, Optional


# -------- Vendor --------
class VendorCreate(BaseModel):
    name: str
    location: Optional[str] = None


class VendorResponse(BaseModel):
    id: int
    name: str
    location: Optional[str] = None

    class Config:
        orm_mode = True


# -------- Product --------
class ProductCreate(BaseModel):
    name: str
    price: int
    vendor_id: int


class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    vendor_id: int

    class Config:
        orm_mode = True
