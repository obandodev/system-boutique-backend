from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.infrastructure.config import DATABASE_URL

engine = create_engine(DATABASE_URL) # Crea el motor de conexión a PostgreSQL usando la URL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Fábrica que crea sesiones (conversaciones temporales con la DB), bind la une al engine
Base = declarative_base() # Clase base de la que heredan todos los modelos

def get_db():
    db = SessionLocal() # Crea la sesion
    try:
        yield db # Pausa - Esto pasa cuando entrega la sesion al endpoint
    finally:
        db.close() # Continua- Esto pasa cuando el endpoint termina
