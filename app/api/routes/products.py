from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(name=product.name, unit=product.unit)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()