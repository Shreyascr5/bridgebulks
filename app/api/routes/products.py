from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate, ProductResponse
from deps import get_db

router = APIRouter()


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    p = Product(**product.dict())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
