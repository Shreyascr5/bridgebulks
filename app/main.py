from fastapi import FastAPI
from db import engine, Base
from api.routes import vendors, products, vendor_products, bulk_orders

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(vendors.router)
app.include_router(products.router)
app.include_router(vendor_products.router)
app.include_router(bulk_orders.router)