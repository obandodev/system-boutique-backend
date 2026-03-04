from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base
from app.shared.timezone import COLOMBIA_TZ

class Role(Base):
    __tablename__ = "roles"

    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    name_rol = Column(String(100), nullable=False, unique= True)
    creation_date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(COLOMBIA_TZ))

    users = relationship("User", back_populates="role")


