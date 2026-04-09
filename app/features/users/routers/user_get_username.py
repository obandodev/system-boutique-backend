from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.users.schemas.user_schema import UserResponse
from app.features.users.services.user_service import UserService
from app.shared.dependencies import require_role

router = APIRouter()

@router.get("/{document}", response_model=UserResponse)
def get_user_by_username(document: str, db: Session = Depends(get_db), current_user: dict = Depends(require_role("Admin"))):
    service = UserService(db)
    return service.get_user_by_document(document)