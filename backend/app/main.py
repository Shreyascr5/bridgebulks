from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import engine, Base
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

@app.get("/")
def root():
    return {"message": "BridgeBulks API Running"}