from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import vendors, products, vendor_products, bulk_orders, customers, analytics, vendor_performance

from app.db import engine, Base
import app.models  # This registers the models

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(vendors.router)
app.include_router(products.router)
app.include_router(vendor_products.router)
app.include_router(bulk_orders.router)
app.include_router(customers.router)
app.include_router(analytics.router)
app.include_router(vendor_performance.router)

# Static dashboard
app.mount("/static", StaticFiles(directory="app/static"), name="static")