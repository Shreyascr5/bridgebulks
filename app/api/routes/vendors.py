from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Vendor
from schemas import VendorCreate, VendorResponse
from deps import get_db

router = APIRouter()


@router.get("/", response_model=list[VendorResponse])
def list_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()


@router.post("/", response_model=VendorResponse)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    v = Vendor(**vendor.dict())
    db.add(v)
    db.commit()
    db.refresh(v)
    return v
