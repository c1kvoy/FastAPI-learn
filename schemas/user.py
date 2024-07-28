from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    title: str
    description: str

    class Config:
        arbitrary_types_allowed = True

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        arbitrary_types_allowed = True

class User(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

class UserCreate(User):
    password: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

class UserUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
