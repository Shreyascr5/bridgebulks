from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Vendor
from deps import get_db

router = APIRouter()


@router.get("/")
def list_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()
