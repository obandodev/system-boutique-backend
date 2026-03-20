from fastapi import APIRouter
from app.features.users.routers.user_create import router as create_router
from app.features.users.routers.user_register import router as register_router
from app.features.users.routers.user_get_all import router as user_get_all

router = APIRouter(prefix="/users", tags=["Users"])
router.include_router(create_router)
router.include_router(register_router)
router.include_router(user_get_all)