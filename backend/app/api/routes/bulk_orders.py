from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(prefix="/bulk-orders", tags=["Bulk Orders"])

@router.post("/")
def create_order(order: schemas.BulkOrderCreate, db: Session = Depends(get_db)):
    new_order = models.BulkOrder(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/my-orders")
def get_my_orders(db: Session = Depends(get_db)):
    # The current schema doesn't implement real customer scoping/auth.
    # This endpoint returns all orders so the UI has data to render.
    orders = db.query(
        models.BulkOrder.id,
        models.BulkOrder.product_id,
        models.BulkOrder.quantity,
        models.BulkOrder.total_price,
        models.Product.name.label("product_name"),
    ).outerjoin(models.Product, models.Product.id == models.BulkOrder.product_id).all()

    return [
        {
            "order_id": o.id,
            "product_id": o.product_id,
            "product_name": o.product_name,
            "quantity": o.quantity,
            "total_price": o.total_price,
            "status": "Placed",  # status tracking is not implemented in the current model
        }
        for o in orders
    ]


@router.get("/")
def list_orders(db: Session = Depends(get_db)):
    return get_my_orders(db=db)