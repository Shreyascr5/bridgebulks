from fastapi import FastAPI
from db import engine, Base
from api.routes import router

app = FastAPI(title="Bridge Bulking Platform")

# Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/")
def root():
    return {"status": "FastAPI + DB ready 🚀"}
