from fastapi import APIRouter
from app.features.roles.routers.role_create import router as role_create
from app.features.roles.routers.role_update import router as role_update
from app.features.roles.routers.role_get_all import router as role_get_all
from app.features.roles.routers.role_get_by_name import router as role_get_by_name


router = APIRouter(prefix="/roles" , tags=["Roles"])
router.include_router(role_create)
router.include_router(role_update)
router.include_router(role_get_all)
router.include_router(role_get_by_name)