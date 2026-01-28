from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from deps import get_db
from models import Customer, Order
from schemas import CustomerCreate, CustomerResponse, OrderCreate, OrderResponse

router = APIRouter()

@router.post("/", response_model=CustomerResponse)
def create_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    customer = Customer(**payload.dict())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


@router.post("/{customer_id}/orders", response_model=OrderResponse)
def place_order(customer_id: int, payload: OrderCreate, db: Session = Depends(get_db)):
    order = Order(customer_id=customer_id, **payload.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("/{customer_id}/orders", response_model=list[OrderResponse])
def list_orders(customer_id: int, db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.customer_id == customer_id).all()
