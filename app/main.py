from fastapi import FastAPI
from db import engine
from models import Base
from api.routes.customers import router as customer_router

app = FastAPI(title="BridgeBulks API")

Base.metadata.create_all(bind=engine)

app.include_router(customer_router)


@app.get("/")
def root():
    return {"status": "BridgeBulks API running 🚀"}
