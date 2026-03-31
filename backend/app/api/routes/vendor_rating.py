from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import VendorPerformance
from app.schemas import VendorRatingCreate, VendorRatingResponse

router = APIRouter(prefix="/vendor-rating", tags=["Vendor Rating"])


@router.post("/", response_model=VendorRatingResponse)
def rate_vendor(rating: VendorRatingCreate, db: Session = Depends(get_db)):
    vendor_perf = db.query(VendorPerformance).filter(
        VendorPerformance.vendor_id == rating.vendor_id
    ).first()

    if vendor_perf:
        vendor_perf.rating = (vendor_perf.rating + rating.rating) / 2
        vendor_perf.on_time_delivery = rating.on_time_delivery
        vendor_perf.quality_score = rating.quality_score
        vendor_perf.total_orders += 1
    else:
        vendor_perf = VendorPerformance(
            vendor_id=rating.vendor_id,
            rating=rating.rating,
            total_orders=1,
            on_time_delivery=rating.on_time_delivery,
            quality_score=rating.quality_score,
        )
        db.add(vendor_perf)

    db.commit()
    db.refresh(vendor_perf)
    return vendor_perf