from pydantic import BaseModel
from datetime import datetime
from app.features.categories.models.category import StateCategoryType

class CategoryCreate(BaseModel):
    name : str
    description : str

class CategoryResponse(BaseModel):
    id_category : int
    name : str
    description : str
    state : StateCategoryType
    creation_date : datetime