from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app import models

router = APIRouter(prefix="/vendor-performance", tags=["Vendor Performance"])

@router.get("/")
def vendor_performance(db: Session = Depends(get_db)):
    results = (
        db.query(
            models.Vendor.name,
            func.sum(models.BulkOrderItem.quantity * models.BulkOrderItem.price_at_order_time).label("revenue"),
            func.count(models.BulkOrderItem.id).label("orders")
        )
        .join(models.BulkOrderItem.vendor_id == models.Vendor.id)
        .group_by(models.Vendor.name)
        .all()
    )

    return results