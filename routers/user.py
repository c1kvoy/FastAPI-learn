from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user_methods import *
from schemas.user import UserCreate, User
from database import SessionLocal

user_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.put("/users/create-user", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@user_router.get("/users/get/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.patch("/users/update/{user_id}", response_model=User)
def update_user_rout(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    return db_user


@user_router.delete("/users/delete/{user_id}")
def delete_user_rout(user_id: int, db: Session = Depends(get_db)):
    if delete_user(db, user_id):
        return {"message": "User deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
