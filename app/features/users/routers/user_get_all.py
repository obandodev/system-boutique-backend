from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.users.schemas.user_schema import UserResponse
from app.features.users.services.user_service import UserService
from app.shared.dependencies import require_role

router = APIRouter()

@router.get("/", response_model=list[UserResponse], dependencies=[Depends(require_role("Admin"))])
def get_all_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()