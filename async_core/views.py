from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException as FastAPIHTTPException
from .models import Product as ProductModel, Base
from .schemas import Product as ProductSchema
from .methods import *
from .db import Session_async, engine

app = FastAPI()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Запускаем создание таблиц при старте приложения
@app.on_event("startup")
async def on_startup():
    await create_tables()


async def get_db():
    async with Session_async() as session:
        yield session


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/product/create", response_model=ProductSchema, tags=["product"])
async def create_item_rout(product: ProductSchema, db=Depends(get_db)):
    db_product = await create_product(product, db)
    if not db_product:
        raise FastAPIHTTPException(status_code=404, detail=f"Ошибка")
    return db_product


@app.get("/product/{name}", response_model=ProductSchema, tags=["product"])
async def read_item_by_name_rout(name: str, db=Depends(get_db)):
    db_product = await read_product_by_name(name, db)
    if not db_product:
        raise FastAPIHTTPException(status_code=404, detail=f"Product with {name} not found")
    else:
        return db_product


@app.patch("/product/{product_name}/update", response_model=ProductSchema, tags=["product"])
async def update_item_rout(product_name: str, product: ProductSchema, db=Depends(get_db)):
    db_product = await update_product(product_name, product, db)
    if not db_product:
        raise FastAPIHTTPException(status_code=414, detail=f"Product with {product_name} not found")
    else:
        return db_product


@app.delete("/product/{product_name}", tags=["product"])
async def delete(name: str, db=Depends(get_db)):
    db_product = await delete_product(name, db)
    if not db_product:
        raise FastAPIHTTPException(status_code=414, detail=f"Product with {name} not found")
    else:
        return {
            "status": "success",
        }
