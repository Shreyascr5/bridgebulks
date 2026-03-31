from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app import models

router = APIRouter(prefix="/analytics", tags=["Analytics"])

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


@router.get("/revenue-by-product")
def revenue_by_product(db: Session = Depends(get_db)):
    rows = (
        db.query(
            models.Product.id.label("product_id"),
            models.Product.name.label("product_name"),
            func.coalesce(func.sum(models.BulkOrder.total_price), 0).label("revenue"),
        )
        .join(models.BulkOrder, models.BulkOrder.product_id == models.Product.id, isouter=True)
        .group_by(models.Product.id, models.Product.name)
        .all()
    )

    return [
        {
            "product_id": r.product_id,
            "product_name": r.product_name,
            "revenue": float(r.revenue),
        }
        for r in rows
    ]


@router.get("/orders-by-product")
def orders_by_product(db: Session = Depends(get_db)):
    rows = (
        db.query(
            models.Product.id.label("product_id"),
            models.Product.name.label("product_name"),
            func.count(models.BulkOrder.id).label("orders"),
        )
        .join(models.BulkOrder, models.BulkOrder.product_id == models.Product.id, isouter=True)
        .group_by(models.Product.id, models.Product.name)
        .all()
    )

    return [
        {
            "product_id": r.product_id,
            "product_name": r.product_name,
            "orders": int(r.orders),
        }
        for r in rows
    ]