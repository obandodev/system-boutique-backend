from app.infrastructure.database import Base
from sqlalchemy import Column,Integer, String, Text, Enum, DateTime, text
from enum import Enum as PyEnum
from datetime import datetime
from app.shared.timezone import COLOMBIA_TZ


class StateCategoryType(PyEnum):
    Active = "Active"
    Inactive = "Inactive"

class Category(Base):
    __tablename__ = "categories"

    id_category = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    state = Column(Enum(StateCategoryType, name="state_category_type_enum"), nullable=False, default=StateCategoryType.Active, server_default=text("'Active'"))
    creation_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(COLOMBIA_TZ))