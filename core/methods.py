from http.client import HTTPException

from core.models import Product as ProductModel
from core.schemas import Product as ProductSchema
from sqlalchemy import select



def create_product(product: ProductSchema, db) -> ProductModel:
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    return db_product
