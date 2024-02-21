from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import select
from database.models import User, Meal
from database.database import engine, Base

app = FastAPI()

@app.get("/")
def index():
    with engine.connect() as session:
        Base.metadata.create_all(engine)
        return session.scalars(select(User)).all()
    return {"matt the pm"}