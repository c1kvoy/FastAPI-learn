from fastapi import FastAPI
from routers import user
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.user_router)

@app.get("/")
async def root():
    return {"Hello": "World"}
