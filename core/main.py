from fastapi import FastAPI
from core.views import main_router, items_router

app = FastAPI()
app.include_router(main_router)
app.include_router(items_router)


