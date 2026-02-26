from pydantic import BaseModel, EmailStr # BaseModel es la clase base de Pydantic que da poderes de validación automática a los schemas
from datetime import datetime

class UserCreate(BaseModel): # Schema para crear un usuario (request)
    name : str
    email : EmailStr # Tipo especial de Pydantic que valida que el string tenga formato de email válido
    password : str

class UserResponse(BaseModel): # Schema para la respuesta de la API (response)
    id : int
    name : str
    email : str
    created_at : datetime

    class Config:
        from_attributes = True # Permite que Pydantic lea objetos de SQLAlchemy y los convierta a diccionario