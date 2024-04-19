import datetime
from typing import Optional
from pydantic import BaseModel, Field
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

# meals table grabs id key from users table, user can filter by date to get meals stored on that day

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), nullable=False, unique=True, index=True)
    hashed_password = Column(String(256), nullable=False)
    meals = relationship("Meal", back_populates="user")

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    meal_name = Column(String, index=True)
    calories = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Meal", back_populates="user")
