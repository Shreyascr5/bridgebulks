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
    vendor_rating,
    order_status
)
from fastapi.middleware.cors import CORSMiddleware


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
app.include_router(order_status.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)