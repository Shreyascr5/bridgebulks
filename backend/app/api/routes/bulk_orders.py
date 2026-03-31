from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter()

@router.post("/")
def create_order(order: schemas.BulkOrderCreate, db: Session = Depends(get_db)):
    new_order = models.BulkOrder(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order