from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas
from app.models import VendorProduct, Vendor, BulkOrder, BulkOrderItem, VendorPerformance
from app.auth import get_current_user
from app.redis_client import redis_client
import json

router = APIRouter(prefix="/bulk-orders", tags=["Bulk Orders"])


def select_best_vendor(db, product_id, quantity):
    cache_key = f"vendor_prices:{product_id}"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        vendors = json.loads(cached_data)
    else:
        vendors = db.query(
            VendorProduct.vendor_id,
            VendorProduct.price,
            Vendor.rating,
            Vendor.delivery_time
        ).join(Vendor, Vendor.id == VendorProduct.vendor_id)\
         .filter(VendorProduct.product_id == product_id).all()

        vendors = [
            {
                "vendor_id": v.vendor_id,
                "price": v.price,
                "rating": v.rating,
                "delivery_time": v.delivery_time
            }
            for v in vendors
        ]

        redis_client.set(cache_key, json.dumps(vendors), ex=300)

    if not vendors:
        return None, 0

    prices = [v["price"] for v in vendors]
    ratings = [v["rating"] for v in vendors]
    delivery_times = [v["delivery_time"] for v in vendors]

    min_price, max_price = min(prices), max(prices)
    min_delivery, max_delivery = min(delivery_times), max(delivery_times)

    best_score = -1
    best_vendor = None
    best_price = 0

    for v in vendors:
        price_score = (max_price - v["price"]) / (max_price - min_price + 0.01)
        rating_score = v["rating"] / 5
        delivery_score = (max_delivery - v["delivery_time"]) / (max_delivery - min_delivery + 0.01)

        score = (0.5 * price_score) + (0.3 * rating_score) + (0.2 * delivery_score)

        if score > best_score:
            best_score = score
            best_vendor = v["vendor_id"]
            best_price = v["price"]

    return best_vendor, best_price

@router.post("/", response_model=schemas.BulkOrderResponse)
def create_bulk_order(
    order: schemas.BulkOrderCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    db_order = BulkOrder(customer_id=user_id, total_price=0)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    total_price = 0
    items_response = []

    for item in order.items:
        vendor_id, price = select_best_vendor(db, item.product_id, item.quantity)

        if vendor_id is None:
            raise HTTPException(status_code=404, detail="No vendor found")

        item_total = price * item.quantity
        total_price += item_total

        # Save bulk order item
        db_item = BulkOrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            vendor_id=vendor_id,
            quantity=item.quantity
        )
        db.add(db_item)

        # Save vendor performance
        performance = VendorPerformance(
            vendor_id=vendor_id,
            order_id=db_order.id,
            rating=4.0,
            delivery_time=3
        )
        db.add(performance)

        items_response.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "vendor_id": vendor_id
        })

    db_order.total_price = total_price
    db.commit()
    db.refresh(db_order)

    return {
        "id": db_order.id,
        "customer_id": db_order.customer_id,
        "total_price": total_price,
        "items": items_response
    }


@router.get("/my-orders")
def get_my_orders(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    orders = db.query(BulkOrder).filter(BulkOrder.customer_id == user_id).all()
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