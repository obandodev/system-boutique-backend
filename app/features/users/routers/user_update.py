from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.users.schemas.user_schema import UserResponse
from app.features.users.services.user_service import UserService
from app.shared.dependencies import require_role

router = APIRouter()
@router.patch("/{username}", response_model=UserResponse, dependencies=[Depends(require_role("Admin"))])
def user_update(username : str, db : Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user(username)