from enum import Enum as PyEnum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum, text
from app.infrastructure.database import Base
from app.shared.timezone import COLOMBIA_TZ

class StateProviderType(PyEnum):
    Active = "Active"
    Inactive = "Inactive"

class Provider(Base):
    __tablename__ = "providers"

    id_provider = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    contact_name = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    state = Column(Enum(StateProviderType, name="state_provider_type_enum"), nullable=False, default=StateProviderType.Active, server_default=text("'Active'"))
    creation_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(COLOMBIA_TZ))