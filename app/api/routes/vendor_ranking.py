from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Vendor

router = APIRouter(prefix="/vendor-ranking", tags=["Vendor Ranking"])


@router.get("/")
def get_vendor_ranking(db: Session = Depends(get_db)):
    vendors = db.query(Vendor).all()

    return sorted(
        [
            {
                "vendor": v.name,
                "rating": v.rating,
                "delivery_time": v.delivery_time,
                "reliability": v.reliability_score
            }
            for v in vendors
        ],
        key=lambda x: (x["rating"], -x["delivery_time"], x["reliability"]),
        reverse=True
    )