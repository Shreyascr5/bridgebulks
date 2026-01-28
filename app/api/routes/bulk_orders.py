from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import BulkOrder
from schemas import BulkOrderCreate
from deps import get_db

router = APIRouter()


@router.post("/")
def create_bulk_order(order: BulkOrderCreate, db: Session = Depends(get_db)):
    bo = BulkOrder(**order.dict())
    db.add(bo)
    db.commit()
    db.refresh(bo)
    return bo
