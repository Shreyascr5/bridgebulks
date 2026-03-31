from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created"}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user and db_user.password == user.password:
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}