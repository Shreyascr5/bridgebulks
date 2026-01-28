from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)


class BulkOrder(Base):
    __tablename__ = "bulk_orders"

    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    items = relationship("BulkOrderItem", back_populates="bulk_order")


class BulkOrderItem(Base):
    __tablename__ = "bulk_order_items"

    id = Column(Integer, primary_key=True)
    bulk_order_id = Column(Integer, ForeignKey("bulk_orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Float, nullable=False)

    bulk_order = relationship("BulkOrder", back_populates="items")
    product = relationship("Product")
