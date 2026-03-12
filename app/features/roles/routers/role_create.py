from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.roles.schemas.role_schema import RoleCreate, RoleResponse
from app.features.roles.services.role_service import RoleService
from app.shared.dependencies import require_role

router = APIRouter()

@router.post("/", response_model=RoleResponse, dependencies=[Depends(require_role("Admin"))])
def create_role(request: RoleCreate, db : Session = Depends(get_db)):
    service = RoleService(db)
    return service.create_role(request.name_rol)