from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app import models

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/")
def get_analytics(db: Session = Depends(get_db)):
    total_orders = db.query(func.count(models.BulkOrder.id)).scalar()
    total_revenue = db.query(func.sum(models.BulkOrder.total_price)).scalar()

    avg_order_value = 0
    if total_orders and total_revenue:
        avg_order_value = total_revenue / total_orders

    return {
        "total_orders": total_orders or 0,
        "total_revenue": total_revenue or 0,
        "average_order_value": avg_order_value
    }