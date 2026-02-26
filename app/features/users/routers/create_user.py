from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.users.services.user_service import UserService
from app.features.users.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model= UserResponse)
def create_user(user: UserCreate, db: Session= Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)
