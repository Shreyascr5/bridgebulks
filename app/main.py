from fastapi import FastAPI

from db import engine
from models import Base
from api.routes.vendors import router as vendor_router
from api.routes.products import router as product_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(vendor_router)
app.include_router(product_router)
