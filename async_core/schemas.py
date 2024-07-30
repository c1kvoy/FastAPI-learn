from pydantic import BaseModel


class Product(BaseModel):
    product_name: str
    description: str | None = None


class Transaction(BaseModel):
    product_id: int
    count: int = 1
