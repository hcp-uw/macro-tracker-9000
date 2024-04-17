from fastapi import FastAPI, Depends, HTTPException, status
# wat we need this for
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# WHO TF IS JOSE
from jose import JWTError, jwt

from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import select
from database.models import User, Meal
from database.database import engine, Base

from database import crud, models, schemas, SessionLocal, engine

from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/meals/", response_model=schemas.Meal)
def create_meal_for_user(
    user_id: int, meal: schemas.MealCreate, db: Session = Depends(get_db), current_user:schemas.User = Depends(get_current_user) # why tf is this not working
):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return crud.create_user_meal(db=db, meal=meal, user_id=user_id)
    
@app.get("/meals/", response_model=list[schemas.Meal])
def read_meals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    meals = crud.get_meals(db, skip=skip, limit=limit)
    return meals
 
@app.get("/users/{user_id}/meals/", response_model=list[schemas.Meal])
def read_user_meals(user_id: int, db: Session = Depends(get_db)):
    meals = crud.get_user_meals(db, user_id = user_id)
    return meals

SECRET_KEY = os.getenv("SECRET_KEY") # where do we get this from
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # why token

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta # fix this later
    else:
        expire = datetime.now(datetime.UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # fix this shit later
    return encode_jwt

# what are async functions for
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWWW-Authenticate:" "Bearer"},
    )
    try:
        # wtf is this payload thing
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("user_id")
        if username is None or user_id is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username, user_id=user_id)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # How do these request forms work
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            deetail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # why is it "sub"
    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id}, expires_delta=access_token_expires
    )