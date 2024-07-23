from fastapi import APIRouter, Body, Header
from core.models import Item, User
from typing import List, Annotated

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
    ]


@items_router.put("/items/{item_id}")
async def get_item(user: Annotated[User, Body(embed=True)], item_id: Annotated[int, None] = 9999):
    return {"item_id": item_id, "user": user}
