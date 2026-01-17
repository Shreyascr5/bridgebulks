from fastapi import FastAPI

from db import engine
from models import Base

from api.routes.vendors import router as vendor_router
from api.routes.products import router as product_router
from api.routes.bulk_orders import router as bulk_order_router

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BridgeBulks API")

# register routers
app.include_router(vendor_router, prefix="/vendors", tags=["Vendors"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(bulk_order_router, prefix="/bulk-orders", tags=["Bulk Orders"])

@app.get("/")
def root():
    return {"status": "BridgeBulks API running 🚀"}
