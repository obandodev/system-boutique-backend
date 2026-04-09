from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.shared.dependencies import require_role
from app.features.providers.schemas.provider_schema import ProviderResponse
from app.features.providers.services.provider_service import ProviderService

router = APIRouter()
@router.patch("/{name}", response_model=ProviderResponse, dependencies=[Depends(require_role("Admin"))])
def provider_update(name : str, db : Session = Depends(get_db)):
    service = ProviderService(db)
    return service.update_provider(name)