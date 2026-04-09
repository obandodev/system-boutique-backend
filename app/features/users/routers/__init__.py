from fastapi import APIRouter
from app.features.users.routers.user_create import router as create_router
from app.features.users.routers.user_get_all import router as user_get_all
from app.features.users.routers.user_me import router as user_me
from app.features.users.routers.user_get_username import router as user_get_username
from app.features.users.routers.user_update import router as user_update
from app.features.users.routers.user_update_info import router as user_update_info

router = APIRouter(prefix="/users", tags=["Usuarios"])
router.include_router(create_router)
router.include_router(user_get_all)
router.include_router(user_me, prefix="/me")  # Ver propio perfil
router.include_router(user_get_username)           
router.include_router(user_update)
router.include_router(user_update_info)