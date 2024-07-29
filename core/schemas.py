from pydantic import BaseModel

class Product(BaseModel):
    product_name : str
    class Config:
        arbitrary_types_allowed = True
