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

    # -----------------------------
    # OPTION 1: SPLIT VENDORS
    # -----------------------------
    split_total = 0
    split_items = []

    for item in order.items:
        vendor_prices = db.query(models.VendorProduct).filter(
            models.VendorProduct.product_id == item.product_id
        ).all()

        best_vendor = None
        best_score = 999999
        best_price = 0

        for vp in vendor_prices:
            vendor = db.query(models.Vendor).filter(models.Vendor.id == vp.vendor_id).first()
            score = (1.0 * vp.price) + (0.5 * vendor.distance) - (0.5 * vendor.rating)

            if score < best_score:
                best_score = score
                best_vendor = vendor
                best_price = vp.price

        item_price = best_price * item.quantity
        split_total += item_price

        split_items.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "vendor_id": best_vendor.id,
            "price": best_price,
            "rating": best_vendor.rating,
            "distance": best_vendor.distance,
            "score": best_score
        })

    # -----------------------------
    # OPTION 2: SINGLE VENDOR
    # -----------------------------
    vendors = db.query(models.Vendor).all()
    best_vendor_total = 999999
    best_vendor_items = []

    for vendor in vendors:
        vendor_total = 0
        vendor_items = []
        possible = True

        for item in order.items:
            vp = db.query(models.VendorProduct).filter(
                models.VendorProduct.vendor_id == vendor.id,
                models.VendorProduct.product_id == item.product_id
            ).first()

            if not vp:
                possible = False
                break

            item_price = vp.price * item.quantity
            vendor_total += item_price

            score = (1.0 * vp.price) + (0.5 * vendor.distance) - (0.5 * vendor.rating)

            vendor_items.append({
                "product_id": item.product_id,
                "quantity": item.quantity,
                "vendor_id": vendor.id,
                "price": vp.price,
                "rating": vendor.rating,
                "distance": vendor.distance,
                "score": score
            })

        if possible and vendor_total < best_vendor_total:
            best_vendor_total = vendor_total
            best_vendor_items = vendor_items

    # -----------------------------
    # CHOOSE BEST OPTION
    # -----------------------------
    if best_vendor_total < split_total:
        final_total = best_vendor_total
        final_items = best_vendor_items
        strategy = "single_vendor"
    else:
        final_total = split_total
        final_items = split_items
        strategy = "split_vendors"

    # -----------------------------
    # SAVE ORDER
    # -----------------------------
    db_order = models.BulkOrder(total_price=final_total)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in final_items:
        db_item = models.BulkOrderItem(
            order_id=db_order.id,
            product_id=item["product_id"],
            quantity=item["quantity"],
            vendor_id=item["vendor_id"]
        )
        db.add(db_item)

        # Update vendor performance
        vendor = db.query(models.Vendor).filter(models.Vendor.id == item["vendor_id"]).first()
        vendor.total_orders += 1
        vendor.total_quantity_supplied += item["quantity"]
        vendor.total_revenue += item["price"] * item["quantity"]

    db.commit()

    return {
        "id": db_order.id,
        "total_price": final_total,
        "items": final_items
    }