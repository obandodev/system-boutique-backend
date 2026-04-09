from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.providers.schemas.provider_schema import ProviderResponse
from app.features.providers.services.provider_service import ProviderService
from app.shared.dependencies import require_role

router = APIRouter()

@router.get("/{name}", response_model=ProviderResponse)
def get_provider_by_name(name : str, db: Session = Depends(get_db), current_user: dict = Depends(require_role("Admin"))):
    service = ProviderService(db)
    return service.get_provider_by_name(name)