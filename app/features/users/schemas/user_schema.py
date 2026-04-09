from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.features.users.models.user import StateUserType, DocumentType
from typing import Optional

class UserCreate(BaseModel):
    name : str
    last_name : str
    type_document : DocumentType
    document : str
    username : str
    phone : str
    email : EmailStr
    password : str
    id_rol : int

class UserResponse(BaseModel):
    id_user : int
    name : str
    last_name : str
    type_document : DocumentType
    document : str
    username : str
    phone : str
    email : EmailStr
    state : StateUserType
    creation_date : datetime
    last_access: Optional[datetime]
    id_rol : int

class UserUpdate(BaseModel):
    name : Optional[str] = None
    last_name : Optional[str] = None
    username : Optional[str] = None
    phone : Optional[str] = None
    email : Optional[EmailStr] = None
