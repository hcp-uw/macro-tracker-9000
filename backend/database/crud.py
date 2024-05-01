from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models, schemas

from passlib.context import CryptContext

import requests
import os

# this is used every time we authenticate the access token provided by the frontend
# whenever the frontend makes an endpoint call
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

# this is used when we check if a username has already been created
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# dont need
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# old get_meals function
# def get_meals(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Meal).offset(skip).limit(limit).all()

# once we have verified that a username hasn't been created,
# save the username and a hashed password to the db
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# create user meals and adds them to the databasee
# meal is associated with the user_id
def create_user_meal(db: Session, meal: schemas.MealCreate):
    db_meal = models.Meal(
        user_id = meal.user_id,
        meal_name = meal.meal_name,
        calories = meal.calories,
        timestamp = meal.timestamp
    )
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal
   
# gets all of a user's meals sorted by timestamp
def get_user_meals(db: Session, user_id: int):
    return db.query(models.Meal).filter(models.Meal.user_id == user_id).order_by(desc(models.Meal.timestamp)).all()


# authentication stuff
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # wtf does this do

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_macros(query):
    base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    api_key = os.getenv("FOODDATA_API_KEY")

    params = {
        "api_key" : api_key,
        "query" : query,
        "dataType" : "Survey (FNDDS)",
        "pageSize" : 1,
        "pageNumber" : 1
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data=response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("erm... error while making API request!", e)
        return None
