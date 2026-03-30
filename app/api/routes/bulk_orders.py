from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models
from app.schemas import BulkOrderCreate
import math

router = APIRouter(prefix="/bulk-orders", tags=["Bulk Orders"])

@router.post("/")
def create_bulk_order(order: BulkOrderCreate, db: Session = Depends(get_db)):
    total_price = 0
    selected_items = []

    for item in order.items:
        inventory_list = db.query(models.Inventory).filter(
            models.Inventory.product_id == item.product_id,
            models.Inventory.stock >= item.quantity
        ).all()

        best_vendor = None
        best_score = -math.inf
        best_price = 0

        for inv in inventory_list:
            vendor = db.query(models.Vendor).filter(models.Vendor.id == inv.vendor_id).first()
            rating = vendor.rating if vendor.rating else 3

            score = (
                (10 / inv.price) * 0.)