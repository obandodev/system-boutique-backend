from fastapi import APIRouter
from app.features.providers.routers.create_provider import router as create_provider

router = APIRouter(prefix="/providers", tags=["Proveedores"])
router.include_router(create_provider)