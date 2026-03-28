from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import BulkOrder, BulkOrderItem, Vendor, Product

router = APIRouter(prefix="/order-history", tags=["Order History"])


@router.get("/customer/{customer_id}")
def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    orders = db.query(BulkOrder).filter(BulkOrder.customer_id == customer_id).all()
    result = []

    for order in orders:
        items = db.query(BulkOrderItem).filter(BulkOrderItem.order_id == order.id).all()
        result.append({
            "order_id": order.id,
            "total_price": order.total_price,
            "items": [
                {
                    "product_id": i.product_id,
                    "vendor_id": i.vendor_id,
                    "quantity": i.quantity
                }
                for i in items
            ]
        })

    return result


@router.get("/vendor/{vendor_id}")
def get_vendor_orders(vendor_id: int, db: Session = Depends(get_db)):
    items = db.query(BulkOrderItem).filter(BulkOrderItem.vendor_id == vendor_id).all()
    result = []

    for item in items:
        order = db.query(BulkOrder).filter(BulkOrder.id == item.order_id).first()
        result.append({
            "order_id": order.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "total_order_price": order.total_price
        })

    return result