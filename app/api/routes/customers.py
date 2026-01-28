from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Customer
from schemas import CustomerCreate, CustomerResponse
from deps import get_db

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    existing = db.query(Customer).filter(Customer.phone == customer.phone).first()
    if existing:
        raise HTTPException(status_code=400, detail="Customer already exists")

    new_customer = Customer(
        name=customer.name,
        phone=customer.phone,
        email=customer.email
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


@router.get("/", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()
