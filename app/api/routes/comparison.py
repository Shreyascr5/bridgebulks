from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models

router = APIRouter(prefix="/comparison", tags=["Comparison"])

@router.get("/{product_id}")
def compare_vendors(product_id: int, db: Session = Depends(get_db)):
    inventory_list = db.query(models.Inventory).filter(
        models.Inventory.product_id == product_id
    ).all()

    vendor_comparison = []
    best_vendor = None
    best_score = -1

    for inv in inventory_list:
        vendor = db.query(models.Vendor).filter(models.Vendor.id == inv.vendor_id).first()
        rating = vendor.rating if vendor.rating else 3

        # Score formula
        score = (
            (10 / inv.price) * 0.5 +
            (rating / 5) * 0.3 +
            (10 / inv.delivery_days) * 0.2
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