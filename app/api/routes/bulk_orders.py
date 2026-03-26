from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
import models, schemas

router = APIRouter(prefix="/bulk-orders", tags=["Bulk Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE BULK ORDER
@router.post("/", response_model=schemas.BulkOrderResponse)
def create_bulk_order(order: schemas.BulkOrderCreate, db: Session = Depends(get_db)):
    total_price = 0
    db_order = models.BulkOrder(vendor_id=None, total_price=0)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    items_response = []

    for item in order.items:
        vendor_price = db.query(models.VendorProduct)\
            .filter(models.VendorProduct.product_id == item.product_id)\
            .order_by(models.VendorProduct.price.asc())\
            .first()

        item_total = vendor_price.price * item.quantity
        total_price += item_total

        db_item = models.BulkOrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            vendor_id=vendor_price.vendor_id,
            quantity=item.quantity
        )
        db.add(db_item)
        db.commit()

        items_response.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "vendor_id": vendor_price.vendor_id
        })

    db_order.total_price = total_price
    db.commit()
    db.refresh(db_order)

    return {
        "id": db_order.id,
        "vendor_id": None,
        "total_price": total_price,
        "items": items_response
    }


# GET ORDER HISTORY
@router.get("/", response_model=list[schemas.BulkOrderResponse])
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(models.BulkOrder).all()

    result = []
    for order in orders:
        items = db.query(models.BulkOrderItem).filter(
            models.BulkOrderItem.order_id == order.id
        ).all()

        item_list = []
        for item in items:
            item_list.append({
                "product_id": item.product_id,
                "quantity": item.quantity,
                "vendor_id": item.vendor_id
            })

        result.append({
            "id": order.id,
            "vendor_id": order.vendor_id,
            "total_price": order.total_price,
            "items": item_list
        })

    return result