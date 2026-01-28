from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Vendor
from schemas import VendorCreate, VendorResponse
from deps import get_db

router = APIRouter()

@router.post("/", response_model=VendorResponse)
def create_vendor(payload: VendorCreate, db: Session = Depends(get_db)):
    vendor = Vendor(**payload.dict())
    db.add(vendor)
    db.commit()
    db.refresh(vendor)
    return vendor

@router.get("/", response_model=list[VendorResponse])
def list_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()
