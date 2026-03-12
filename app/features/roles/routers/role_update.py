from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.roles.schemas.role_schema import  RoleResponse
from app.features.roles.services.role_service import RoleService
from app.shared.dependencies import require_role

router = APIRouter()
@router.patch("/{name_rol}", response_model=RoleResponse, dependencies=[Depends(require_role("Admin"))])
def role_update(name_rol: str, db: Session = Depends(get_db)):
    service = RoleService(db)
    return service.update_role(name_rol)