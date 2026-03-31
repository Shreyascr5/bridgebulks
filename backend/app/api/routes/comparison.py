from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models

router = APIRouter(prefix="/comparison", tags=["Comparison"])

@router.get("/{product_id}")
def compare_vendors(product_id: int, db: Session = Depends(get_db)):
    # `Inventory` model is not present in the current DB schema.
    # `VendorProduct` already contains the needed fields (vendor_id, price, delivery_days).
    vendor_products = db.query(models.VendorProduct).filter(
        models.VendorProduct.product_id == product_id
    ).all()

    vendor_comparison = []
    best_vendor = None
    best_score = -1

    for inv in vendor_products:
        vendor = db.query(models.Vendor).filter(models.Vendor.id == inv.vendor_id).first()
        # Vendor.rating isn't implemented in the current schema, so default to 3.
        rating = getattr(vendor, "rating", None) or 3

        # Score formula
        score = (
            ((10 / inv.price) if inv.price else 0) * 0.5 +
            (rating / 5) * 0.3 +
            ((10 / inv.delivery_days) if inv.delivery_days else 0) * 0.2
        )

        vendor_data = {
            "vendor_id": inv.vendor_id,
            "vendor_name": vendor.name,
            "price": inv.price,
            "rating": rating,
            "delivery_days": inv.delivery_days,
            "score": round(score, 3)
        }

        vendor_comparison.append(vendor_data)

        if score > best_score:
            best_score = score
            best_vendor = vendor_data

    return {
        "vendors": vendor_comparison,
        "selected_vendor": best_vendor
    }