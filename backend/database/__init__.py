from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


host = os.getenv("DATABASE_HOST")
user = os.getenv("DATABASE_USERNAME")
passwd = os.getenv("DATABASE_PASSWORD")
db = os.getenv("DATABASE")

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{passwd}@{host}/{db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)