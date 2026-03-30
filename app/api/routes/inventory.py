from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models
from pydantic import BaseModel

router = APIRouter(prefix="/inventory", tags=["Inventory"])

class InventoryCreate(BaseModel):
    vendor_id: int
    product_id: int
    price: float
    stock: int
    delivery_days: int

@router.post("/")
def create_inventory(item: InventoryCreate, db: Session = Depends(get_db)):
    inv = models.Inventory(**item.dict())
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

@router.get("/")
def get_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()