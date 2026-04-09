from sqlalchemy.orm import Session
from app.features.providers.models.provider import Provider
from app.features.providers.models.provider import StateProviderType
from app.features.providers.schemas.provider_schema import ProviderCreate, ProviderUpdate
from app.features.providers.repositories.provider_repository import ProviderRepository
from app.features.providers.validators.providers_validators import validate_provider_name_not_exists, validate_provider_name_exists, validate_provider_exists, validate_provider_name_not_exists_for_update

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
    
    def update_provider_info(self, id_provider : int, data : ProviderUpdate)->Provider:
        provider = self.provider_repository.get_by_id(id_provider)
        validate_provider_exists(provider, id_provider)
        if data.name is not None:
            validate_provider_name_not_exists_for_update(self.db, data.name, provider.id_provider)
        return self.provider_repository.update(provider, data)
    
    def update_provider(self, name : str) ->Provider:
        existing_provider = self.provider_repository.get_by_name(name)
        validate_provider_name_exists(existing_provider, name)
        new_state = StateProviderType.Inactive if existing_provider.state == StateProviderType.Active else StateProviderType.Active
        return self.provider_repository.update_state(name, new_state)
    
    def get_all_providers(self) -> list[Provider]:
        return self.provider_repository.get_all_providers()
    
    def get_provider_by_name(self, name: str) ->Provider:
        provider = self.provider_repository.get_by_name(name)
        validate_provider_name_exists(provider, name)
        return provider