from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate, ProductResponse
from deps import get_db

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    product = Product(**payload.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
