from uuid import UUID

from pydantic import BaseModel, Field
from typing import List, Optional


class User(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(default="dus")
    email: str = Field(min_length=1, max_length=100)


class UserIn(User):
    password: str = Field(min_length=8, max_length=100)


class UserOut(User):
    pass


class UserInDb(User):
    hashed_password: str = Field(min_length=8, max_length=100)


class Item(BaseModel):
    name: str = Field(min_length=1, default="Item", examples=["A very nice Item"])
    price: float = Field(ge=0, default=None)
