from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
import models, schemas

router = APIRouter(prefix="/vendors", tags=["Vendors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.VendorResponse)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    db_vendor = models.Vendor(name=vendor.name)
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor