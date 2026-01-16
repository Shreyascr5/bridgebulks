from fastapi import FastAPI
from db import Base, engine
from api.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
