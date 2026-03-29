from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import models
from app.db import engine

from app.api.routes import (
    vendors,
    products,
    vendor_products,
    bulk_orders,
    customers,
    analytics,
    auth,
    vendor_performance,
    vendor_rating
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(vendors.router)
app.include_router(products.router)
app.include_router(vendor_products.router)
app.include_router(bulk_orders.router)
app.include_router(customers.router)
app.include_router(analytics.router)
app.include_router(auth.router)
app.include_router(vendor_performance.router)
app.include_router(vendor_rating.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")