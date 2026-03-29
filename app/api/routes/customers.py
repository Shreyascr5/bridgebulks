from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/")
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    new_customer = models.Customer(name=customer.name, email=customer.email)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@router.get("/")
def get_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

@router.get("/me")
def get_current_customer(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == user_id).first()
    return {
        "id": customer.id,
        "email": customer.email
    }