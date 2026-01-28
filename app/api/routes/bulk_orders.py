from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from models import BulkOrder, BulkOrderItem
from schemas import BulkOrderCreate, BulkOrderResponse
from deps import get_db

router = APIRouter(prefix="/bulk-orders", tags=["Bulk Orders"])


@router.post("/", response_model=BulkOrderResponse)
def create_bulk_order(payload: BulkOrderCreate, db: Session = Depends(get_db)):
    order = BulkOrder(vendor_id=payload.vendor_id)
    db.add(order)
    db.flush()

    for item in payload.items:
        db.add(
            BulkOrderItem(
                bulk_order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
        )

    db.commit()

    order = (
        db.query(BulkOrder)
        .options(joinedload(BulkOrder.items).joinedload("product"))
        .filter(BulkOrder.id == order.id)
        .first()
    )

    return {
        "id": order.id,
        "vendor_id": order.vendor_id,
        "items": [
            {
                "id": i.id,
                "product_id": i.product_id,
                "product_name": i.product.name,
                "quantity": i.quantity
            }
            for i in order.items
        ]
    }
