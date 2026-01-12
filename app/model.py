from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db import Base

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    location = Column(String)
    created_at = Column(DateTime, server_default=func.now())


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price_per_unit = Column(Integer, nullable=False)
    min_bulk_quantity = Column(Integer, nullable=False)
