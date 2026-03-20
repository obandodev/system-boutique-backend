from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.users.schemas.user_schema import UserRegister, UserResponse
from app.features.users.services.user_service import UserService

router = APIRouter()

@router.post("/register", response_model=UserResponse) # Endpoint Publico
def register_user(request: UserRegister, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.register_user(request)