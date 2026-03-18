from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import BulkOrder, BulkOrderItem, VendorProduct, Product
from schemas import BulkOrderCreate, BulkOrderResponse, BulkOrderItemResponse
from deps import get_db

router = APIRouter(prefix="/bulk-orders", tags=["Bulk Orders"])


@router.post("/", response_model=BulkOrderResponse)
def create_bulk_order(payload: BulkOrderCreate, db: Session = Depends(get_db)):

    total_price = 0
    response_items = []

    order = BulkOrder(vendor_id=None)
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in payload.items:

        vps = db.query(VendorProduct).filter(
            VendorProduct.product_id == item.product_id
        ).all()

        if not vps:
            raise Exception(f"No pricing for product {item.product_id}")

        cheapest_vp = min(vps, key=lambda x: x.price)

        item_total = item.quantity * cheapest_vp.price
        total_price += item_total

        product = db.query(Product).filter(Product.id == item.product_id).first()

        order_item = BulkOrderItem(
            bulk_order_id=order.id,
            product_id=item.product_id,
            vendor_id=cheapest_vp.vendor_id,   # STORE VENDOR
            quantity=item.quantity
        )
        db.add(order_item)
        db.commit()
        db.refresh(order_item)

        response_items.append(
            BulkOrderItemResponse(
                id=order_item.id,
                product_id=product.id,
                product_name=product.name,
                vendor_id=cheapest_vp.vendor_id,   #  RETURN VENDOR
                quantity=item.quantity
            )
        )

    return {
        "id": order.id,
        "vendor_id": None,
        "total_price": total_price,
        "items": response_items
    }