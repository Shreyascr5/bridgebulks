from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import BulkOrder
from app.schemas import OrderStatusUpdate, OrderStatusResponse

router = APIRouter(prefix="/order-status", tags=["Order Status"])


@router.post("/", response_model=OrderStatusResponse)
def update_order_status(status_update: OrderStatusUpdate, db: Session = Depends(get_db)):
    order = db.query(BulkOrder).filter(BulkOrder.id == status_update.order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status_update.status
    db.commit()

    return {"message": f"Order status updated to {status_update.status}"}


@router.get("/{order_id}")
def get_order_status(order_id: int, db: Session = Depends(get_db)):
    order = db.query(BulkOrder).filter(BulkOrder.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "order_id": order.id,
        "status": order.status
    }