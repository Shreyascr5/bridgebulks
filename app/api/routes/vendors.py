from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Vendor
from schemas import VendorCreate, VendorResponse
from deps import get_db

router = APIRouter(prefix="/vendors", tags=["Vendors"])

# ✅ CREATE VENDOR (THIS WAS MISSING)
@router.post("/", response_model=VendorResponse)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    new_vendor = Vendor(name=vendor.name)
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    return new_vendor


# ✅ GET ALL VENDORS
@router.get("/", response_model=list[VendorResponse])
def get_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()