from core import db
from core.models import Product as ProductModel
from core.schemas import Product as ProductSchema
from sqlalchemy import select, update, delete


def create_product(product: ProductSchema, db) -> ProductModel:
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()

    return db_product

def read_product_by_name(name: str, db) -> ProductModel:
    query = select(ProductModel).where(ProductModel.product_name == name)
    result = db.execute(query).first()
    if not result:
        return False

    else:
        db_product = result[0]
        return db_product

def update_product(name: str, product: ProductSchema, db) -> ProductModel:
    query = select(ProductModel).where(ProductModel.product_name == name)
    result = db.execute(query).first()
    if result is None:
        return None
    db_product = result[0]
    db.execute(update(ProductModel).where(ProductModel.product_name == name).values(**product.dict(exclude_unset=True)))
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(name: str, db) -> ProductModel:
    query = select(ProductModel).where(ProductModel.product_name == name)
    result = db.execute(query).first()
    if result is None:
        return False
    else:
        db.execute(delete(ProductModel).where(ProductModel.product_name == name))
        db.commit()
        return True