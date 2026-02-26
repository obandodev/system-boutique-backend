from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    codigo : str
    name : str
    color : str
    marca : str

class ProductResponse(BaseModel):
    id : int
    codigo : str
    name : str
    color : str
    marca : str
    created_at : datetime

    class Config:
        from_attributes = True

