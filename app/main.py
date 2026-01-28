from fastapi import FastAPI
from db import Base, engine

from api.routes.vendors import router as vendor_router
from api.routes.products import router as product_router
from api.routes.bulk_orders import router as bulk_order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="BridgeBulks API")

app.include_router(vendor_router)
app.include_router(product_router)
app.include_router(bulk_order_router)
