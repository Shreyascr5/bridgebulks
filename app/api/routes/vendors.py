from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import Vendor, Product
from schemas import VendorCreate, VendorResponse, ProductResponse

from schemas import VendorCreate, VendorResponse, ProductResponse

router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"]
)

@router.get("/", response_model=list[VendorResponse])
def list_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()

@router.post("/", response_model=VendorResponse)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    v = Vendor(**vendor.model_dump())
    db.add(v)
    db.commit()
    db.refresh(v)
    return v

@router.get("/{vendor_id}/products", response_model=list[ProductResponse])
def vendor_products(vendor_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.vendor_id == vendor_id).all()
