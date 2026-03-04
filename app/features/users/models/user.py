from enum import Enum as PyEnum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum, text, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base
from app.shared.timezone import COLOMBIA_TZ

class DocumentType(PyEnum):
    TI = "TI"
    CC = "CC"

class StateUserType(PyEnum):
    Active = "Active"
    Inactive = "Inactive"


class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    type_document = Column(Enum(DocumentType, name="document_type_enum"), nullable=False)
    document = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(100), nullable=False)
    state = Column(Enum(StateUserType, name="state_user_type_enum"), nullable=False, default=StateUserType.Active, server_default=text("'Active'"))
    creation_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(COLOMBIA_TZ))
    last_access = Column(DateTime(timezone=True), nullable=True)
    id_rol = Column(Integer, ForeignKey("roles.id_rol"), nullable=False)

    role = relationship("Role", back_populates="users")



