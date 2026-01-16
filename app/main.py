from fastapi import FastAPI
from db import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def health():
    return {"status": "FastAPI is running cleanly 🚀"}
