from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import BulkOrder, BulkOrderItem, VendorProduct, Product
from schemas import BulkOrderCreate, BulkOrderResponse, BulkOrderItemResponse
from deps import get_db

router = APIRouter(prefix="/bulk-orders", tags=["Bulk Orders"])


@router.post("/", response_model=BulkOrderResponse)
def create_bulk_order(payload: BulkOrderCreate, db: Session = Depends(get_db)):
    
    # 1️⃣ Create bulk order
    order = BulkOrder(vendor_id=payload.vendor_id)
    db.add(order)
    db.commit()
    db.refresh(order)

    response_items = []
    total_price = 0

    # 2️⃣ Loop through items
    for item in payload.items:

        # 🔍 Get product
        product = db.query(Product).filter(Product.id == item.product_id).first()

        # 🔍 Get price from VendorProduct
        vp = db.query(VendorProduct).filter(
            VendorProduct.vendor_id == payload.vendor_id,
            VendorProduct.product_id == item.product_id
        ).first()

        if not vp:
            raise Exception(f"No price set for product {item.product_id}")

        item_total = item.quantity * vp.price
        total_price += item_total

        # 3️⃣ Save item
        order_item = BulkOrderItem(
            bulk_order_id=order.id,
            product_id=item.product_id,
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
                quantity=item.quantity
            )
        )

    # 🔥 PRINT total (for now)
    print("TOTAL PRICE:", total_price)

    return {
        "id": order.id,
        "vendor_id": order.vendor_id,
        "items": response_items
    }