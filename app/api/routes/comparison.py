from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import VendorProduct

router = APIRouter(prefix="/comparison", tags=["Vendor Comparison"])


@router.get("/{product_id}")
def compare_vendors(product_id: int, db: Session = Depends(get_db)):
    vendor_products = db.query(VendorProduct).filter(
        VendorProduct.product_id == product_id
    ).all()

    if not vendor_products:
        return {"message": "No vendors found"}

    lowest_price = min(v.price for v in vendor_products)
    fastest_delivery = min(v.delivery_days for v in vendor_products)

    vendor_list = []
    best_score = 0
    best_vendor = None

    for vp in vendor_products:
        price_score = lowest_price / vp.price
        rating_score = vp.vendor.rating / 5 if vp.vendor.rating else 0
        delivery_score = fastest_delivery / vp.delivery_days

        score = (0.5 * price_score) + (0.3 * rating_score) + (0.2 * delivery_score)

        vendor_data = {
            "vendor_id": vp.vendor.id,
            "vendor_name": vp.vendor.name,
            "price": vp.price,
            "rating": vp.vendor.rating,
            "delivery_days": vp.delivery_days,
            "score": round(score, 3)
        }

        vendor_list.append(vendor_data)

        if score > best_score:
            best_score = score
            best_vendor = vendor_data

    return {
        "vendors": vendor_list,
        "selected_vendor": best_vendor
    }