from pydantic import BaseModel

class Product(BaseModel):
    product_name : str
    description : str | None = None
    class Config:
        arbitrary_types_allowed = True
