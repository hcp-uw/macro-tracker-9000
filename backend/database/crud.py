from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models, schemas

from passlib.context import CryptContext

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# dont need
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# dont need
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# old get_meals function
def get_meals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meal).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

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
   
def get_user_meals(db: Session, user_id: int):
    return db.query(models.Meal).filter(models.Meal.user_id == user_id).order_by(desc(models.Meal.timestamp)).all()

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