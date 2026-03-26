from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.providers.schemas.provider_schema import ProviderResponse
from app.features.providers.services.provider_service import ProviderService
from app.shared.dependencies import require_role

router = APIRouter()

@router.get("/", response_model=list[ProviderResponse], dependencies=[Depends(require_role("Admin"))])
def get_all_providers(db: Session = Depends(get_db)):
    service= ProviderService(db)
    return service.get_all_providers()
