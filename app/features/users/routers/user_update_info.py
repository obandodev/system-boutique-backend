from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.users.schemas.user_schema import UserUpdate, UserResponse
from app.features.users.services.user_service import UserService
from app.shared.dependencies import get_current_user

router = APIRouter()

@router.patch("/{document}/info", response_model=UserResponse)
def update_user_info(document: str, data: UserUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = UserService(db)
    return service.update_user_info(document, data, current_user)