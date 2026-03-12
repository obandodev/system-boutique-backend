from pydantic import BaseModel
from datetime import datetime
from app.features.roles.models.rol import StateRolType

class RoleCreate(BaseModel):
    name_rol : str 

class RoleStateUpdate(BaseModel):
    state : StateRolType 

class RoleResponse(BaseModel):
    id_rol : int
    name_rol : str
    state: StateRolType
    creation_date : datetime 