from sqlalchemy.orm import Session
from app.features.providers.models.provider import Provider

class ProviderRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, name : str, contact_name : str, phone : str) -> Provider:
        provider = Provider(
            name=name,
            contact_name=contact_name,
            phone=phone
        )
        self.db.add(provider)
        self.db.commit()
        self.db.refresh(provider)
        return provider

    def update(self, provider, data) -> Provider:
        if data.name is not None:
            provider.name = data.name
        if data.contact_name is not None:
            provider.contact_name = data.contact_name
        if data.phone is not None:
            provider.phone = data.phone
        self.db.commit()
        self.db.refresh(provider)
        return provider
    
    def get_by_id(self, id_provider: int) -> Provider:
        return self.db.query(Provider).filter(Provider.id_provider == id_provider).first()
    
    def get_by_name(self, name: str) ->Provider:
        return self.db.query(Provider).filter(Provider.name == name).first()

    def get_all_providers(self) ->list[Provider]:
        return self.db.query(Provider).all()
    
    def update_state(self, name : str, state) ->Provider:
        provider = self.get_by_name(name)
        provider.state = state
        self.db.commit()
        self.db.refresh(provider)
        return provider



