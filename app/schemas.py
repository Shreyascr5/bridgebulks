from pydantic import BaseModel

class VendorCreate(BaseModel):
    name: str
    email: str
    location: str | None = None

class VendorResponse(VendorCreate):
    id: int

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    name: str
    price_per_unit: int
    min_bulk_quantity: int

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True
