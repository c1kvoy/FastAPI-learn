from fastapi import FastAPI, Depends
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


@app.post("/product/create", response_model=ProductSchema)
def create_item_rout(product: ProductSchema, db=Depends(get_db)):
    db_product = create_product(product, db)
    return db_product
