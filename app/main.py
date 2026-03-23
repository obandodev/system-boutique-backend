from fastapi import FastAPI
from app.features.auth.routers.login import router as login
from app.features.roles.routers import router as roles_router
from app.features.users.routers import router as users_router
from app.features.providers.routers import router as providers_router


app = FastAPI(title="API-SYSTEM-BOUTIQUE", version="1.0.0")

app.include_router(login)
app.include_router(roles_router)
app.include_router(users_router)
app.include_router(providers_router)