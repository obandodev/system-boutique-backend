from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.users.schemas.user_schema import UserResponse
from app.features.users.services.user_service import UserService
from app.shared.dependencies import get_current_user

router = APIRouter()

@router.get("", response_model=UserResponse)
def get_my_profile(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = UserService(db)
    return service.get_my_profile(current_user["sub"])