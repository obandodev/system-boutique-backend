from enum import Enum as PyEnum
from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime, Enum, text
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base
from app.shared.timezone import COLOMBIA_TZ

class StateRolType(PyEnum):
    Active = "Active"
    Inactive = "Inactive"

class Role(Base):
    __tablename__ = "roles"

    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    name_rol = Column(String(100), nullable=False, unique= True)
    state = Column(Enum(StateRolType, name="state_rol_type"), nullable=False, default=StateRolType.Active, server_default=text("'Active'"))
    creation_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(COLOMBIA_TZ))

    users = relationship("User", back_populates="role")