from fastapi import FastAPI
from fastapi.routing import APIRouter
from app.features.auth.routers.login import router as login
from app.features.roles.routers import router as roles_router
from app.features.users.routers import router as users_router
from app.features.providers.routers import router as providers_router
from app.features.categories.routers import router as categories_routers

app = FastAPI(title="API-SYSTEM-BOUTIQUE", version="1.0.0")

v1 = APIRouter(prefix="/v1")

v1.include_router(login)
v1.include_router(roles_router)
v1.include_router(users_router)
v1.include_router(providers_router)
v1.include_router(categories_routers)

app.include_router(v1)