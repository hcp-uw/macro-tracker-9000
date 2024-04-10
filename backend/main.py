from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import select
from database.models import User, Meal
from database.database import engine, Base

from database import crud, models, schemas, SessionLocal, engine

from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/meals/", response_model=schemas.Meal)
def create_meal_for_user(
    user_id: int, meal: schemas.MealCreate, db: Session = Depends(get_db)
):
    return crud.create_user_meal(db=db, meal=meal, user_id=user_id)
    
@app.get("/meals/", response_model=list[schemas.Meal])
def read_meals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    meals = crud.get_meals(db, skip=skip, limit=limit)
    return meals

@app.get("/users/{user_id}/meals/", response_model=list[schemas.Meal])
def read_user_meals(user_id: int, db: Session = Depends(get_db)):
    meals = crud.get_user_meals(db, user_id = user_id)
    return meals