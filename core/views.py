from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException as FastAPIHTTPException
from core.models import Product as ProductModel, Base
from core.schemas import Product as ProductSchema
from core.methods import *
from core.db import Session, engine

Base.metadata.create_all(bind=engine)
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/product/create", response_model=ProductSchema, tags=["product"])
def create_item_rout(product: ProductSchema, db=Depends(get_db)):
    db_product = create_product(product, db)
    if not db_product:
        raise FastAPIHTTPException(status_code=404, detail=f"Ошибка")
    return db_product


@app.get("/product/{name}", response_model=ProductSchema, tags=["product"])
def read_item_by_name_rout(name: str, db=Depends(get_db)):
    db_product = read_product_by_name(name, db)
    if not db_product:
        raise FastAPIHTTPException(status_code=404, detail=f"Product with {name} not found")
    else:
        return db_product

@app.patch("/product/{product_name}/update", response_model=ProductSchema, tags=["product"])
def update_item_rout(product_name: str , product: ProductSchema, db=Depends(get_db)):
    db_product = update_product(product_name, product, db)
    if not db_product:
        raise FastAPIHTTPException(status_code=414, detail=f"Product with {product_name} not found")
    else:
        return db_product

@app.delete("/product/{product_name}", tags=["product"])
def delete(name: str, db=Depends(get_db)):
    db_product = delete_product(name, db)
    if not db_product:
        raise FastAPIHTTPException(status_code=414, detail=f"Product with {name} not found")
    else:
        return {
            "status": "success",
        }