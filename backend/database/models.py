from typing import Optional
from pydantic import BaseModel, Field
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    hashed_password = Column(String(256))

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), index=True)
    calories = Column(Integer, index=True)
    owner_id = Column(Integer, key="users.id")