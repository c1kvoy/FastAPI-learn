from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional


class User(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None


class UserCreate(User):
    password: Optional[str] = None


class UserUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
