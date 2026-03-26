from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
import models
from sqlalchemy import func

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_analytics(db: Session = Depends(get_db)):
    total_orders = db.query(func.count(models.BulkOrder.id)).scalar()
    total_revenue = db.query(func.sum(models.BulkOrder.total_price)).scalar()

    avg_order_value = 0
    if total_orders and total_revenue:
        avg_order_value = total_revenue / total_orders

    vendors = db.query(models.Vendor).all()

    vendor_data = []
    for v in vendors:
        avg_price = 0
        if v.total_quantity_supplied > 0:
            avg_price = v.total_revenue / v.total_quantity_supplied

        vendor_data.append({
            "vendor_name": v.name,
            "total_revenue": v.total_revenue,
            "items_supplied": v.total_quantity_supplied,
            "times_selected": v.total_orders,
            "average_price": avg_price,
            "rating": v.rating,
            "distance": v.distance
        })

    return {
        "total_bulk_orders": total_orders or 0,
        "total_revenue": float(total_revenue or 0),
        "average_order_value": float(avg_order_value),
        "vendor_performance": vendor_data
    }