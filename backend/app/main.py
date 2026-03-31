from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import engine, Base
from app.db import SessionLocal
from app import models
from app.api.routes import (
    auth,
    vendors,
    products,
    vendor_products,
    bulk_orders,
    analytics,
    comparison,
    vendor_performance,
)

Base.metadata.create_all(bind=engine)

def seed_dummy_data() -> None:
    """
    Seed minimal, consistent demo data for the presentation.
    We only seed when the tables are empty to avoid duplicating rows.
    """
    db = SessionLocal()
    try:
        # Seed user
        if db.query(models.User).count() == 0:
            db.add(models.User(email="demo@bridgebulks.com", password="demo"))

        # Seed vendors
        vendor_names = ["Vendor A", "Vendor B", "Vendor C"]
        existing_vendors = {v.name: v for v in db.query(models.Vendor).all()}
        for name in vendor_names:
            if name not in existing_vendors:
                db.add(models.Vendor(name=name))

        db.commit()

        vendors = {v.name: v for v in db.query(models.Vendor).all()}

        # Seed products
        product_specs = [
            ("Product 1", 20.0),
            ("Product 2", 35.0),
            ("Product 3", 50.0),
        ]
        existing_products = {p.name: p for p in db.query(models.Product).all()}
        for name, price in product_specs:
            if name not in existing_products:
                db.add(models.Product(name=name, price=price))

        db.commit()

        products = {p.name: p for p in db.query(models.Product).all()}

        # Seed vendor-products (join table) only if empty
        if db.query(models.VendorProduct).count() == 0:
            # vendor A/B/C each supply all products with different delivery days
            vendor_list = list(vendors.values())
            product_list = list(products.values())
            for v_idx, v in enumerate(vendor_list):
                for p_idx, p in enumerate(product_list):
                    # price slightly varied by vendor/product index
                    offer_price = float(p.price) * (0.85 + 0.05 * v_idx + 0.01 * p_idx)
                    db.add(
                        models.VendorProduct(
                            vendor_id=v.id,
                            product_id=p.id,
                            price=offer_price,
                            stock=100 - 10 * p_idx,
                            delivery_days=2 + v_idx + p_idx,
                        )
                    )

        # Seed bulk orders (only if empty)
        if db.query(models.BulkOrder).count() == 0:
            # Create a few orders for analytics charts
            product_list = list(db.query(models.Product).all())
            if product_list:
                for i, p in enumerate(product_list[:3]):
                    qty = 2 + i
                    total_price = float(p.price) * qty * 0.9
                    db.add(
                        models.BulkOrder(
                            product_id=p.id,
                            quantity=qty,
                            total_price=total_price,
                        )
                    )

        db.commit()
    finally:
        db.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(vendors.router)
app.include_router(products.router)
app.include_router(vendor_products.router)
app.include_router(bulk_orders.router)
app.include_router(analytics.router)
app.include_router(comparison.router)
app.include_router(vendor_performance.router)

# Seed after routers are registered and tables exist.
# (Safe for demo; guarded by table emptiness checks.)
seed_dummy_data()

@app.get("/")
def root():
    return {"message": "BridgeBulks API Running"}