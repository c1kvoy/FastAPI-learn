from sqlalchemy.orm import Session
from models.user import User as userMD
from schemas.user import UserUpdate, UserCreate
from fastapi import APIRouter

user_router = APIRouter()


def create_user(db: Session, user: UserCreate):
    user_in_db = userMD(email=user.email, username=user.username, password=user.password)
    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)
    return user_in_db


def get_user(db: Session, user_id: int):
    return db.query(userMD).filter(userMD.id == user_id).first()


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    user_in_db = db.query(userMD).filter(userMD.id == user_id).first()

    if not user_in_db:
        return None

    update_data = user_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user_in_db, key, value)

    db.commit()
    db.refresh(user_in_db)
    return user_in_db

    db.commit()
    db.refresh(user_in_db)
    return user_in_db


def delete_user(db: Session, user_id: int):
    user_in_db = db.query(userMD).filter(userMD.id == user_id).first()
    if not user_in_db: return False
    db.delete(user_in_db)
    db.commit()
    return True
