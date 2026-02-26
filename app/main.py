from fastapi import FastAPI
from app.features.users.routers import router as user_router
from app.features.products.routers.create_product import router as create_product


app = FastAPI(title="API-REST", version="1.0.0")
app.include_router(user_router)
app.include_router(create_product)
