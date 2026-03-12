
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.roles.schemas.role_schema import RoleResponse
from app.features.roles.services.role_service import RoleService
from app.shared.dependencies import get_current_user

router = APIRouter()

@router.get("/{name_rol}", response_model=RoleResponse)
def get_role_by_name(name_rol: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = RoleService(db)
    return service.get_role_by_name(name_rol, current_user)