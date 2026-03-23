from sqlalchemy.orm import Session
from app.features.providers.models.provider import Provider
from app.features.providers.schemas.provider_schema import ProviderCreate
from app.features.providers.repositories.provider_repository import ProviderRepository
from app.features.providers.validators.providers_validators import validate_provider_name_not_exists

class ProviderService:
    def __init__(self, db : Session):
        self.db = db
        self.provider_repository = ProviderRepository(db)
    
    def create_provider(self, data : ProviderCreate) -> Provider:
        validate_provider_name_not_exists(self.db, data.name)
        return self.provider_repository.create(
            name=data.name,
            contact_name=data.contact_name,
            phone=data.phone
        )