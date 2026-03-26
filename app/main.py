from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import init_db

from api.routes.vendors import router as vendor_router
from api.routes.products import router as product_router
from api.routes.vendor_products import router as vendor_product_router
from api.routes.bulk_orders import router as bulk_order_router
from api.routes.analytics import router as analytics_router

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

app.include_router(vendor_router)
app.include_router(product_router)
app.include_router(vendor_product_router)
app.include_router(bulk_order_router)
app.include_router(analytics_router)

app.mount("/static", StaticFiles(directory="static"), name="static")