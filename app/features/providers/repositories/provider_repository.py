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
    
    def get_all_providers(self) ->list[Provider]:
        return self.db.query(Provider).all()