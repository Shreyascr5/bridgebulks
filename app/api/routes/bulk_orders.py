from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(prefix="/bulk-orders", tags=["Bulk Orders"])


@router.post("/")
def create_bulk_order(order: schemas.BulkOrderCreate, db: Session = Depends(get_db)):
    total_price = 0
    order_items = []

    # Create order first
    new_order = models.BulkOrder(customer_id=order.customer_id, total_price=0)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in order.items:
        # Find cheapest vendor for this product
        vendor_price = (
            db.query(models.VendorProduct)
            .filter(models.VendorProduct.product_id == item.product_id)
            .order_by(models.VendorProduct.price)
            .first()
        )

        if vendor_price is None:
            continue

        price = vendor_price.price * item.quantity
        total_price += price

        order_item = models.BulkOrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            vendor_id=vendor_price.vendor_id,
            quantity=item.quantity,
            price_at_order_time=vendor_price.price
        )
        db.add(order_item)
        order_items.append(order_item)

    new_order.total_price = total_price
    db.commit()

    return {
        "order_id": new_order.id,
        "total_price": total_price,
        "items": order_items
    }


@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.BulkOrder).all()