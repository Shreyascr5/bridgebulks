from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from deps import get_db
from models import Vendor
from schemas import VendorCreate

router = APIRouter()

@router.post("/vendors")
def create_vendor(
    vendor: VendorCreate,
    db: Session = Depends(get_db)
):
    new_vendor = Vendor(
        name=vendor.name,
        location=vendor.location
    )
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    return new_vendor
