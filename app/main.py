from fastapi import FastAPI
import models
from db import engine

from api.routes.vendors import router as vendor_router
from api.routes.products import router as product_router
from api.routes.vendor_products import router as vendor_product_router
from api.routes.bulk_orders import router as bulk_order_router
from api.routes.vendor_performance import router as vendor_performance_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(vendor_router)
app.include_router(product_router)
app.include_router(vendor_product_router)
app.include_router(bulk_order_router)
app.include_router(vendor_performance_router)