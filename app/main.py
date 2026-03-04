from fastapi import FastAPI
from app.features.auth.routers.login import router as login


app = FastAPI(title="API-REST", version="1.0.0")
app.include_router(login)

from app.features.users.models.user import User
from app.features.roles.models.rol import Role