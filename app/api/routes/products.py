# app/api/routes/products.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# app/api/routes/products.py
from models import Product
from schemas import ProductCreate, ProductResponse
from db import get_db


router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
