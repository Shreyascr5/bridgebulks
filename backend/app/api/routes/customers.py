from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas
from app.security import get_current_user
from passlib.hash import bcrypt

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hash(customer.password)

    new_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        password=hashed_password
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


@router.get("/me", response_model=schemas.CustomerResponse)
def get_current_customer(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(models.Customer).filter(models.Customer.id == user_id).first()