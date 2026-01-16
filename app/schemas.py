from pydantic import BaseModel


# ---------- User ----------
class UserCreate(BaseModel):
    email: str
    password: str


# ---------- Vendor ----------
class VendorCreate(BaseModel):
    name: str
    location: str


class VendorResponse(BaseModel):
    id: int
    name: str
    location: str

    class Config:
        from_attributes = True


# ---------- Product ----------
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
        from_attributes = True
