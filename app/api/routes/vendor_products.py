from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(prefix="/vendor-products", tags=["Vendor Pricing"])

@router.post("/")
def add_vendor_price(data: schemas.VendorProductCreate, db: Session = Depends(get_db)):
    vp = models.VendorProduct(
        vendor_id=data.vendor_id,
        product_id=data.product_id,
        price=data.price
    )
    db.add(vp)
    db.commit()
    db.refresh(vp)
    return vp

@router.get("/")
def get_vendor_prices(db: Session = Depends(get_db)):
    return db.query(models.VendorProduct).all()