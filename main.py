from fastapi import FastAPI
from routers import user
from database import engine
import models

models.Base.metadata.create_all(bind=engine)
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    }
]
app = FastAPI()

app.include_router(user.user_router)

@app.get("/")
async def root():
    return {"Hello": "World"}
