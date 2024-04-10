from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# old get_meals function
def get_meals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meal).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password)
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