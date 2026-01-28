from pydantic import BaseModel


class VendorCreate(BaseModel):
    name: str
    location: str


class VendorResponse(VendorCreate):
    id: int

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    name: str
    price: int
    vendor_id: int


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True


class BulkOrderCreate(BaseModel):
    vendor_id: int


class BulkOrderItemCreate(BaseModel):
    product_id: int
    quantity: int
