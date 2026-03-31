from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class VendorCreate(BaseModel):
    name: str

class Vendor(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    price: float

class BulkOrderCreate(BaseModel):
    product_id: int
    quantity: int
    total_price: float

class VendorProductCreate(BaseModel):
    vendor_id: int
    product_id: int
    price: float
    stock: int
    delivery_days: int

class VendorProduct(BaseModel):
    id: int
    vendor_id: int
    product_id: int
    price: float
    stock: int
    delivery_days: int

    class Config:
        orm_mode = True


