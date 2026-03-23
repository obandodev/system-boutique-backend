from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.providers.schemas.provider_schema import ProviderCreate, ProviderResponse
from app.features.providers.services.provider_service import ProviderService
from app.shared.dependencies import require_role

router = APIRouter()

@router.post("/", response_model=ProviderResponse)
def create_provider(request : ProviderCreate, db : Session = Depends(get_db), current_user: dict = Depends(require_role("Admin"))):
    service = ProviderService(db)
    return service.create_provider(request)