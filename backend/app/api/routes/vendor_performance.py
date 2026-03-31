from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app import models

router = APIRouter(prefix="/vendor-performance", tags=["Vendor Performance"])

@router.get("/")
def get_vendor_performance(db: Session = Depends(get_db)):
    data = db.query(
        models.Vendor.name,
        func.avg(models.VendorRating.rating).label("avg_rating")
    ).join(models.VendorRating, models.Vendor.id == models.VendorRating.vendor_id)\
     .group_by(models.Vendor.name).all()

    return data