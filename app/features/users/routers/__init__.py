from fastapi import APIRouter
from .create_user import router as create_router
from .get_all_users import router as get_all_router

router = APIRouter(prefix="/users", tags=["users"])
router.include_router(create_router)
router.include_router(get_all_router)