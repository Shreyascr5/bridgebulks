# app/api/routes/vendors.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# app/api/routes/vendors.py
from models import Vendor
from schemas import VendorCreate, VendorResponse
from db import get_db


router = APIRouter(prefix="/vendors", tags=["Vendors"])


@router.post("/", response_model=VendorResponse)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    db_vendor = Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor


@router.get("/", response_model=list[VendorResponse])
def list_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()
