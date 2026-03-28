from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(prefix="/vendors", tags=["Vendors"])

@router.post("/")
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    new_vendor = models.Vendor(name=vendor.name)
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    return new_vendor

@router.get("/")
def get_vendors(db: Session = Depends(get_db)):
    return db.query(models.Vendor).all()