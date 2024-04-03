from typing import Optional
from pydantic import BaseModel, Field
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

# meals table grabs id key from users table, user can filter by date to get meals stored on that day

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    hashed_password = Column(String(256))

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, index=True)
    meal_name = Column(String(80), index=True)
    calories = Column(Integer, index=True)