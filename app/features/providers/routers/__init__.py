from fastapi import APIRouter
from app.features.providers.routers.create_provider import router as create_provider
from app.features.providers.routers.provider_get_all import router as provider_get_all
from app.features.providers.routers.provider_get_name import router as provider_get_name
from app.features.providers.routers.provider_update import router as provider_update
from app.features.providers.routers.provider_update_info import router as provider_update_info

router = APIRouter(prefix="/providers", tags=["Proveedores"])
router.include_router(create_provider)
router.include_router(provider_get_all)
router.include_router(provider_get_name)
router.include_router(provider_update)
router.include_router(provider_update_info)