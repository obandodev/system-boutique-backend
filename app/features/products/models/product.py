from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.infrastructure.database import Base
from app.shared.timezone import COLOMBIA_TZ

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, nullable=True, unique=True)
    name = Column(String, nullable=True,)
    color = Column(String, nullable=True)
    marca = Column(String, nullable=True)
    created_at = Column(DateTime, default= lambda: datetime.now(COLOMBIA_TZ))
