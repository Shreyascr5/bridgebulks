from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app import models

router = APIRouter()

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    total_orders = db.query(models.BulkOrder).count()
    total_revenue = db.query(func.sum(models.BulkOrder.total_price)).scalar()
    avg_order = db.query(func.avg(models.BulkOrder.total_price)).scalar()

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue or 0,
        "average_order_value": avg_order or 0
    }