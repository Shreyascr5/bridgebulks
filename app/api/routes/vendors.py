from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from deps import get_db
from models import Vendor
from schemas import VendorCreate, VendorResponse

router = APIRouter(prefix="/vendors", tags=["Vendors"])

@router.post("/", response_model=VendorResponse)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    db_vendor = Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor
