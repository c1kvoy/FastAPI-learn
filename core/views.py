from fastapi import APIRouter, Body
from core.models import *
from typing import Annotated, Dict

main_router = APIRouter()
items_router = APIRouter()


@main_router.get("/")
async def root():
    return {"Hello": "World"}


@items_router.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
        Item(name="ROOOKUS", price=3123133123123)
    ]


@items_router.put("/items/{item_id}")
async def get_item(user: Annotated[User, Body(embed=True)], item_id: Annotated[int, None] = 9999):
    return {"item_id": item_id, "user": user}


def hashing(password: str) -> str:
    return "huy" + password


def user_save_in_db(user_in: UserIn) -> UserInDb:
    hashed_password = hashing(user_in.password)
    user_in_db = UserInDb(**user_in.dict(), hashed_password=hashed_password)
    return user_in_db


users_passwords: Dict[int, str] = {}


@main_router.post("/usercreate", response_model=UserOut, response_model_exclude={"name"} )
async def create_user(user_in: UserIn):
    user_in_db = user_save_in_db(user_in)
    users_passwords[user_in_db.id] = user_in_db.hashed_password
    print(users_passwords)
    return user_in_db
