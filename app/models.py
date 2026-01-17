from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# --------------------
# Vendor
# --------------------
class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)

    products = relationship("Product", back_populates="vendor")


# --------------------
# Product
# --------------------
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    vendor = relationship("Vendor", back_populates="products")


# --------------------
# Bulk Order
# --------------------
class BulkOrder(Base):
    __tablename__ = "bulk_orders"

    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, nullable=False)
    status = Column(String, default="PENDING")

    items = relationship(
        "BulkOrderItem",
        back_populates="order",
        cascade="all, delete"
    )


# --------------------
# Bulk Order Item
# --------------------
class BulkOrderItem(Base):
    __tablename__ = "bulk_order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("bulk_orders.id"))
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("BulkOrder", back_populates="items")
