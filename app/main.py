from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
import time

from app.db import engine
from app.models import Base

app = FastAPI(title="Bridge Bulking Platform")

@app.on_event("startup")
def startup():
    retries = 5
    for i in range(retries):
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database ready, tables created")
            return
        except OperationalError:
            print(f"⏳ DB not ready, retry {i+1}/{retries}")
            time.sleep(3)

    raise Exception("❌ Database not available after retries")

@app.get("/")
def health():
    return {"status": "API + DB running correctly 🚀"}
