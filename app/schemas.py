from pydantic import BaseModel
from datetime import datetime


class CustomerCreate(BaseModel):
    name: str
    phone: str
    email: str | None = None


class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: str | None
    created_at: datetime

    class Config:
        from_attributes = True
