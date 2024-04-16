import datetime
from pydantic import BaseModel

class Meal(BaseModel):
    id: int
    user_id: int
    meal_name: str
    calories: int
    timestamp: datetime

    class Config:
        orm_mode = True

class MealCreate(BaseModel):
    user_id: int
    meal_name: str
    calories: int
    timestamp: datetime

class User(BaseModel):
    id: int
    username: str
    password: str
    meals: list[Meal] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    user_id: int | None = None

# Why don't we make any changes in the models.py to include tokens?