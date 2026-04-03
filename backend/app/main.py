import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import engine, Base, SessionLocal
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

# ---------------------------------------------------------------------------
# Create all DB tables on startup
# ---------------------------------------------------------------------------
Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------------------------
# Seed minimal demo data (only when tables are empty)
# ---------------------------------------------------------------------------
def seed_dummy_data() -> None:
    db = SessionLocal()
    try:
        if db.query(models.User).count() == 0:
            db.add(models.User(email="demo@bridgebulks.com", password="demo"))

        vendor_names = ["Vendor A", "Vendor B", "Vendor C"]
        existing_vendors = {v.name: v for v in db.query(models.Vendor).all()}
        for name in vendor_names:
            if name not in existing_vendors:
                db.add(models.Vendor(name=name))
        db.commit()

        vendors_map = {v.name: v for v in db.query(models.Vendor).all()}

        product_specs = [("Product 1", 20.0), ("Product 2", 35.0), ("Product 3", 50.0)]
        existing_products = {p.name: p for p in db.query(models.Product).all()}
        for name, price in product_specs:
            if name not in existing_products:
                db.add(models.Product(name=name, price=price))
        db.commit()

        products_map = {p.name: p for p in db.query(models.Product).all()}

        if db.query(models.VendorProduct).count() == 0:
            for v_idx, v in enumerate(vendors_map.values()):
                for p_idx, p in enumerate(products_map.values()):
                    offer_price = float(p.price) * (0.85 + 0.05 * v_idx + 0.01 * p_idx)
                    db.add(models.VendorProduct(
                        vendor_id=v.id,
                        product_id=p.id,
                        price=round(offer_price, 2),
                        stock=100 - 10 * p_idx,
                        delivery_days=2 + v_idx + p_idx,
                    ))

        if db.query(models.BulkOrder).count() == 0:
            product_list = list(db.query(models.Product).all())
            for i, p in enumerate(product_list[:3]):
                qty = 2 + i
                db.add(models.BulkOrder(
                    product_id=p.id,
                    quantity=qty,
                    total_price=round(float(p.price) * qty * 0.9, 2),
                ))

        db.commit()
    except Exception as e:
        db.rollback()
        print(f"[seed] Error during seeding: {e}")
    finally:
        db.close()


# ---------------------------------------------------------------------------
# App + CORS
# ---------------------------------------------------------------------------
app = FastAPI(title="BridgeBulks API", version="1.0.0")

# Read the deployed frontend URL from environment.
# Set FRONTEND_URL in your Render backend service environment variables.
FRONTEND_URL = os.getenv("FRONTEND_URL", "").strip()

origins = [
    "https://bridgebulks-frontend.onrender.com",  # production frontend
    "http://localhost:5173",                        # local Vite dev server
    "http://localhost:3000",
]

# Also allow whatever is set in the env variable (handles custom domains)
if FRONTEND_URL and FRONTEND_URL not in origins:
    origins.append(FRONTEND_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
app.include_router(auth.router)
app.include_router(vendors.router)
app.include_router(products.router)
app.include_router(vendor_products.router)
app.include_router(bulk_orders.router)
app.include_router(analytics.router)
app.include_router(comparison.router)
app.include_router(vendor_performance.router)


@app.get("/")
def root():
    return {"message": "BridgeBulks API Running"}


# Seed after app + tables are fully ready
seed_dummy_data()
