from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get("/")
def get_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()