from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Customer
from app.schemas import CustomerCreate, CustomerResponse
from app.auth import get_current_user

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(
        name=customer.name,
        email=customer.email,
        password=customer.password
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@router.get("/me", response_model=CustomerResponse)
def get_current_customer_data(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    customer = db.query(Customer).filter(Customer.id == user_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer