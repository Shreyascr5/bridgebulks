from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/vendor-products", tags=["Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add inventory
@router.post("/")
def add_vendor_product(item: schemas.VendorProductCreate, db: Session = Depends(get_db)):
    new_item = models.VendorProduct(
        vendor_id=item.vendor_id,
        product_id=item.product_id,
        price=item.price,
        stock=item.stock,
        delivery_days=item.delivery_days
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Get inventory
@router.get("/")
def get_vendor_products(db: Session = Depends(get_db)):
    return db.query(models.VendorProduct).all()