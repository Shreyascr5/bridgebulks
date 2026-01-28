from fastapi import FastAPI
from db import engine, Base

from api.routes.vendors import router as vendor_router
from api.routes.products import router as product_router
from api.routes.bulk_orders import router as bulk_order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="BridgeBulks API")

app.include_router(vendor_router, prefix="/vendors", tags=["vendors"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(bulk_order_router, prefix="/bulk-orders", tags=["bulk-orders"])


@app.get("/")
def root():
    return {"status": "BridgeBulks API running"}
