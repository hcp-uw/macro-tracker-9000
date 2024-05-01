import datetime
from pydantic import BaseModel

class MealBase(BaseModel):
    user_id: int
    meal_name: str
    calories: int

class MealCreate(MealBase):
    timestamp:datetime

class MealUpdate(MealBase):
    new_calories: int

class Meal(MealBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# class Meal(BaseModel):
#     id: int
#     user_id: int
#     meal_name: str
#     calories: int
#     timestamp: datetime

#     class Config:
#         orm_mode = True

# class MealCreate(BaseModel):
#     user_id: int
#     meal_name: str
#     calories: int
#     timestamp: datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    meals: list[Meal] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: int | None = None

# Why don't we make any changes in the models.py to include tokens?