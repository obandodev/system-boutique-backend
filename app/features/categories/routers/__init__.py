from fastapi import APIRouter
from app.features.categories.routers.create_category import router as create_category
from app.features.categories.routers.category_get_all import router as category_get_all

router = APIRouter(prefix="/categories" , tags=["Categorias"])
router.include_router(create_category)
router.include_router(category_get_all)
