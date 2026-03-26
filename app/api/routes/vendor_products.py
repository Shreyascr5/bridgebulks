from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
import models, schemas

router = APIRouter(prefix="/vendor-products", tags=["Vendor Pricing"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_vendor_product(data: schemas.VendorProductCreate, db: Session = Depends(get_db)):
    vp = models.VendorProduct(**data.dict())
    db.add(vp)
    db.commit()
    db.refresh(vp)
    return vp