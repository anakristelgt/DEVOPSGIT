from typing import List, Dict

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.responses import RedirectResponse

app = FastAPI() #Objeto asignado a FastAPI

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/") #Decorador
async def root(): #Función asíncrona
    return {"message":"Hello World!"}

@app.get("/myname/{name}") #Decorador
async def myName(name: str): #Función asíncrona
    return {"message": f"Hello {name}, this is my new API!"}

@app.get("/picture") #Decorador
async def pict(): #Función asíncrona
    return RedirectResponse('https://images.pexels.com/photos/12708081/pexels-photo-12708081.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')

@app.post("/users/create", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)


@app.post("/users/{user_id}/", response_model=schemas.UserBase)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)


@app.post("/users/", response_model=List[schemas.UserData])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db=db)