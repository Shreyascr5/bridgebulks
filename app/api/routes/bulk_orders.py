from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import BulkOrder
from deps import get_db

router = APIRouter()


@router.get("/")
def list_bulk_orders(db: Session = Depends(get_db)):
    return db.query(BulkOrder).all()
