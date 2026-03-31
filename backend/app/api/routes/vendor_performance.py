from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app import models

router = APIRouter(prefix="/vendor-performance", tags=["Vendor Performance"])

@router.get("/")
def get_vendor_performance(db: Session = Depends(get_db)):
    # The current schema does not include a `VendorRating` table.
    # To keep the UI working, derive "performance" from `VendorProduct`.
    # - avg_delivery: average delivery_days per vendor
    # - total_orders: number of vendor-product rows (proxy for orders)
    # - avg_rating: constant default (rating is not tracked yet)
    rows = (
        db.query(
            models.Vendor.name.label("vendor"),
            func.avg(models.VendorProduct.delivery_days).label("avg_delivery"),
            func.count(models.VendorProduct.id).label("total_orders"),
        )
        .join(models.VendorProduct, models.VendorProduct.vendor_id == models.Vendor.id)
        .group_by(models.Vendor.id, models.Vendor.name)
        .all()
    )

    return [
        {
            "vendor": r.vendor,
            "avg_rating": 3,
            "avg_delivery": float(r.avg_delivery) if r.avg_delivery is not None else 0,
            "total_orders": int(r.total_orders),
        }
        for r in rows
    ]