from fastapi import FastAPI
from app.features.auth.routers.login import router as login
from app.features.roles.routers import router as roles_router


app = FastAPI(title="API-BARBER-APP", version="1.0.0")
app.include_router(login)
app.include_router(roles_router)