from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
import models

router = APIRouter(prefix="/vendor-performance", tags=["Vendor Performance"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_vendor_performance(db: Session = Depends(get_db)):
    vendors = db.query(models.Vendor).all()

    result = []
    for v in vendors:
        avg_price = 0
        if v.total_quantity_supplied > 0:
            avg_price = v.total_revenue / v.total_quantity_supplied

        result.append({
            "vendor_id": v.id,
            "name": v.name,
            "total_orders": v.total_orders,
            "total_quantity_supplied": v.total_quantity_supplied,
            "total_revenue": v.total_revenue,
            "average_price": avg_price,
            "rating": v.rating,
            "distance": v.distance
        })

    return result