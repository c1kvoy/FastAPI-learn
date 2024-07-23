from uuid import UUID

from pydantic import BaseModel, Field
from typing import List


class Item(BaseModel):
    name: str = Field(min_length=1, default="Item", examples=["A very nice Item"])
    price: float = Field(ge=0, default=None)


class User(BaseModel):
    id: int = Field(ge=0, default=None)
    name: str = Field(min_length=1, default="User")
    best_items: List[Item]
