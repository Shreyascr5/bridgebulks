from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import get_db
from app import models

router = APIRouter(prefix="/analytics", tags=["Analytics"])


# Overall analytics
@router.get("/")
def get_analytics(db: Session = Depends(get_db)):
    total_orders = db.query(func.count(models.BulkOrder.id)).scalar()
    total_revenue = db.query(func.sum(models.BulkOrder.total_price)).scalar()

    avg_order_value = 0
    if total_orders:
        avg_order_value = total_revenue / total_orders

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "average_order_value": avg_order_value
    }


# Monthly spending
@router.get("/monthly")
def monthly_spending(db: Session = Depends(get_db)):
    data = db.query(
        func.date_trunc('month', models.BulkOrder.created_at).label("month"),
        func.sum(models.BulkOrder.total_price)
    ).group_by("month").all()

    return [{"month": str(d[0]), "total": d[1]} for d in data]


# Top products
@router.get("/top-products")
def top_products(db: Session = Depends(get_db)):
    data = db.query(
        models.BulkOrderItem.product_id,
        func.sum(models.BulkOrderItem.quantity).label("total_qty")
    ).group_by(models.BulkOrderItem.product_id).order_by(func.sum(models.BulkOrderItem.quantity).desc()).all()

    return [{"product_id": d[0], "total_quantity": d[1]} for d in data]


# Vendor revenue
@router.get("/vendor-revenue")
def vendor_revenue(db: Session = Depends(get_db)):
    data = db.query(
        models.BulkOrderItem.vendor_id,
        func.sum(models.VendorProduct.price * models.BulkOrderItem.quantity).label("revenue")
    ).join(
        models.VendorProduct,
        (models.VendorProduct.vendor_id == models.BulkOrderItem.vendor_id) &
        (models.VendorProduct.product_id == models.BulkOrderItem.product_id)
    ).group_by(models.BulkOrderItem.vendor_id).all()

    return [{"vendor_id": d[0], "revenue": float(d[1])} for d in data]


# Order trend
@router.get("/order-trend")
def order_trend(db: Session = Depends(get_db)):
    data = db.query(
        func.date(models.BulkOrder.created_at),
        func.count(models.BulkOrder.id)
    ).group_by(func.date(models.BulkOrder.created_at)).all()

    return [{"date": str(d[0]), "orders": d[1]} for d in data]