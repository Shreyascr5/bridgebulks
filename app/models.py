from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db import Base
import datetime


class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    unit = Column(String)


class VendorProduct(Base):
    __tablename__ = "vendor_products"
    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    price = Column(Float)


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)


class BulkOrder(Base):
    __tablename__ = "bulk_orders"
    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_price = Column(Float)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    items = relationship("BulkOrderItem", back_populates="order")


class BulkOrderItem(Base):
    __tablename__ = "bulk_order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("bulk_orders.id"))
    product_id = Column(Integer)
    vendor_id = Column(Integer)
    quantity = Column(Integer)
    price_at_order_time = Column(Float)

    order = relationship("BulkOrder", back_populates="items")