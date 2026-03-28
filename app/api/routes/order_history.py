from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models

router = APIRouter(prefix="/order-history", tags=["Order History"])


@router.get("/")
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(models.BulkOrder).all()

    result = []
    for order in orders:
        order_data = {
            "order_id": order.id,
            "customer_id": order.customer_id,
            "total_price": order.total_price,
            "created_at": order.created_at,
            "items": []
        }

        for item in order.items:
            order_data["items"].append({
                "product_id": item.product_id,
                "vendor_id": item.vendor_id,
                "quantity": item.quantity
            })

        result.append(order_data)

    return result


@router.get("/customer/{customer_id}")
def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    orders = db.query(models.BulkOrder).filter(models.BulkOrder.customer_id == customer_id).all()

    result = []
    for order in orders:
        result.append({
            "order_id": order.id,
            "total_price": order.total_price,
            "created_at": order.created_at
        })

    return result