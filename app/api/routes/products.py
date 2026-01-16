from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import Product, Vendor
from schemas import ProductCreate, ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    vendor = db.query(Vendor).filter(Vendor.id == product.vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    p = Product(**product.model_dump())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
