from fastapi import APIRouter
from app.features.providers.routers.create_provider import router as create_provider
from app.features.providers.routers.provider_get_all import router as provider_get_all

router = APIRouter(prefix="/providers", tags=["Proveedores"])
router.include_router(create_provider)
router.include_router(provider_get_all)