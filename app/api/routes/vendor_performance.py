from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app.models import VendorPerformance, Vendor

router = APIRouter(prefix="/vendor-performance", tags=["Vendor Performance"])


@router.get("/")
def get_vendor_performance(db: Session = Depends(get_db)):
    data = db.query(
        Vendor.name,
        func.avg(VendorPerformance.rating).label("avg_rating"),
        func.avg(VendorPerformance.delivery_time).label("avg_delivery"),
        func.count(VendorPerformance.id).label("total_orders")
    ).join(Vendor, Vendor.id == VendorPerformance.vendor_id)\
     .group_by(Vendor.name).all()

    return [
        {
            "vendor": d[0],
            "avg_rating": float(d[1]),
            "avg_delivery": float(d[2]),
            "total_orders": d[3]
        }
        for d in data
    ]