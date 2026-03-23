from pydantic import BaseModel
from datetime import datetime
from app.features.providers.models.provider import StateProviderType

class ProviderCreate(BaseModel):
    name : str
    contact_name : str
    phone : str

class ProviderResponse(BaseModel):
    id_provider : int
    name : str
    contact_name : str
    phone : str
    state : StateProviderType
    creation_date : datetime