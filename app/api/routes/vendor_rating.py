from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import VendorPerformance, BulkOrder
from app.schemas import VendorRatingCreate, VendorRatingResponse

router = APIRouter(prefix="/vendor-rating", tags=["Vendor Rating"])


@router.post("/", response_model=VendorRatingResponse)
def rate_vendor(rating: VendorRatingCreate, db: Session = Depends(get_db)):
    order = db.query(BulkOrder).filter(BulkOrder.id == rating.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    performance = VendorPerformance(
        vendor_id=rating.vendor_id,
        order_id=rating.order_id,
        rating=rating.rating,
        delivery_time=rating.delivery_time
    )

    db.add(performance)
    db.commit()

    return {"message": "Vendor rating submitted successfully"}