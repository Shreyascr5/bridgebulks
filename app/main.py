from fastapi import FastAPI
from db import engine
from models import Base
from api.routes.products import router as product_router
from api.routes.vendors import router as vendor_router

app = FastAPI(title="BridgeBulks API")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(vendor_router)
app.include_router(product_router)

@app.get("/")
def root():
    return {"status": "BridgeBulks API running 🚀"}
