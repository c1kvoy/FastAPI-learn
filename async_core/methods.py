from sqlalchemy.ext.asyncio import AsyncSession
from .models import Product as ProductModel
from .schemas import Product as ProductSchema
from sqlalchemy import update, delete
from sqlalchemy.future import select as future_select

async def create_product(product: ProductSchema, db: AsyncSession) -> ProductModel:
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def read_product_by_name(name: str, db: AsyncSession) -> ProductModel:
    query = future_select(ProductModel).where(ProductModel.product_name == name)
    result = await db.execute(query)
    db_product = result.scalar_one_or_none()
    return db_product

async def update_product(name: str, product: ProductSchema, db: AsyncSession) -> ProductModel:
    query = future_select(ProductModel).where(ProductModel.product_name == name)
    result = await db.execute(query)
    db_product = result.scalar_one_or_none()
    if db_product is None:
        return None
    await db.execute(
        update(ProductModel)
        .where(ProductModel.product_name == name)
        .values(**product.dict(exclude_unset=True))
    )
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def delete_product(name: str, db: AsyncSession) -> bool:
    query = future_select(ProductModel).where(ProductModel.product_name == name)
    result = await db.execute(query)
    db_product = result.scalar_one_or_none()
    if db_product is None:
        return False
    await db.execute(delete(ProductModel).where(ProductModel.product_name == name))
    await db.commit()
    return True
