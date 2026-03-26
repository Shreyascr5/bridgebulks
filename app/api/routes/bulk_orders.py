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


@router.post("/", response_model=schemas.BulkOrderResponse)
def create_bulk_order(order: schemas.BulkOrderCreate, db: Session = Depends(get_db)):

    total_price = 0
    order_items_response = []

    db_order = models.BulkOrder(total_price=0)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        product_id = item.product_id
        quantity = item.quantity

        vendor_prices = db.query(models.VendorProduct).filter(
            models.VendorProduct.product_id == product_id
        ).all()

        best_vendor = None
        best_score = 999999
        best_price = 0
        best_rating = 0
        best_distance = 0

        for vp in vendor_prices:
            vendor = db.query(models.Vendor).filter(models.Vendor.id == vp.vendor_id).first()

            score = (1.0 * vp.price) + (0.5 * vendor.distance) - (0.5 * vendor.rating)

            if score < best_score:
                best_score = score
                best_vendor = vendor
                best_price = vp.price
                best_rating = vendor.rating
                best_distance = vendor.distance

        item_price = best_price * quantity
        total_price += item_price

        # Update vendor performance
        best_vendor.total_orders += 1
        best_vendor.total_quantity_supplied += quantity
        best_vendor.total_revenue += item_price

        db_item = models.BulkOrderItem(
            order_id=db_order.id,
            product_id=product_id,
            quantity=quantity,
            vendor_id=best_vendor.id
        )
        db.add(db_item)

        order_items_response.append({
            "product_id": product_id,
            "quantity": quantity,
            "vendor_id": best_vendor.id,
            "price": best_price,
            "rating": best_rating,
            "distance": best_distance,
            "score": best_score
        })

    db_order.total_price = total_price
    db.commit()

    return {
        "id": db_order.id,
        "total_price": total_price,
        "items": order_items_response
    }