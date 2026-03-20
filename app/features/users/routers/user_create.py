from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.users.schemas.user_schema import UserCreate, UserResponse
from app.features.users.services.user_service import UserService
from app.shared.dependencies import require_role

router = APIRouter()

@router.post("/", response_model=UserResponse) # Endpoint Privado
def create_user(request: UserCreate, db: Session = Depends(get_db), current_user: dict = Depends(require_role("Admin"))):
    service = UserService(db)
    return service.create_user(request)