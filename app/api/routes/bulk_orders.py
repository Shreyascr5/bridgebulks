from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import BulkOrder, BulkOrderItem
from schemas import BulkOrderCreate, BulkOrderResponse, BulkOrderItemCreate

router = APIRouter(
    prefix="/bulk-orders",
    tags=["Bulk Orders"]
)


@router.post("/", response_model=BulkOrderResponse)
def create_bulk_order(data: BulkOrderCreate, db: Session = Depends(get_db)):
    order = BulkOrder(**data.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.post("/{bulk_order_id}/add-item")
def add_item(
    bulk_order_id: int,
    item: BulkOrderItemCreate,
    db: Session = Depends(get_db)
):
    order = db.query(BulkOrder).filter(BulkOrder.id == bulk_order_id).first()
    if not order or order.status != "open":
        raise HTTPException(status_code=400, detail="Bulk order not open")

    bulk_item = BulkOrderItem(
        bulk_order_id=bulk_order_id,
        **item.model_dump()
    )
    db.add(bulk_item)
    db.commit()
    return {"message": "Item added to bulk order"}
