from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

DATABASE_URL = "postgresql://postgres:postgres@postgres:5432/bulkdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    import models
    retries = 10
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            print("Database connected and tables created")
            return
        except Exception as e:
            print("Database not ready, retrying in 5 seconds...")
            time.sleep(5)
            retries -= 1
    print("Failed to connect to database.")