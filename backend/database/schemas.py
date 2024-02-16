from pydantic import BaseModel

class MealBase(BaseModel):
    name:str
    calories: int | None = None

class MealCreate(MealBase):
    pass

class Meal(MealBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    meals: list[Meal] = []