from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.infrastructure.database import Base
from app.shared.timezone import COLOMBIA_TZ

class User(Base): # Base es la encargada de hacer que los modelos la hereden para reconocerlas como tablas
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False,)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(COLOMBIA_TZ))
