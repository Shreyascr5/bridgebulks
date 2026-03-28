from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app import models

router = APIRouter(prefix="/vendor-performance", tags=["Vendor Performance"])

@router.get("/vendor-performance/")
def vendor_performance(db: Session = Depends(get_db)):
    data = db.query(
        models.Vendor.name,
        func.sum(models.VendorProduct.price * models.BulkOrderItem.quantity).label("revenue"),
        func.count(models.BulkOrderItem.id).label("orders")
    ).join(models.BulkOrderItem, models.BulkOrderItem.vendor_id == models.Vendor.id)\
     .join(models.VendorProduct,
           (models.VendorProduct.vendor_id == models.BulkOrderItem.vendor_id) &
           (models.VendorProduct.product_id == models.BulkOrderItem.product_id))\
     .group_by(models.Vendor.name).all()

    return [
        {"vendor": d[0], "revenue": float(d[1] or 0), "orders": d[2]}
        for d in data
    ]

    # return results