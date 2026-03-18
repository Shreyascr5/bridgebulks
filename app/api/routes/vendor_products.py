from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import VendorProduct
from schemas import VendorProductCreate, VendorProductResponse
from deps import get_db

router = APIRouter(prefix="/vendor-products", tags=["Vendor Products"])

@router.post("/", response_model=VendorProductResponse)
def create_vendor_product(payload: VendorProductCreate, db: Session = Depends(get_db)):
    vp = VendorProduct(**payload.dict())
    db.add(vp)
    db.commit()
    db.refresh(vp)
    return vp

@router.get("/", response_model=list[VendorProductResponse])
def list_vendor_products(db: Session = Depends(get_db)):
    return db.query(VendorProduct).all()