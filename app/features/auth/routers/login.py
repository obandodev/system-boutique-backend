from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.auth.schemas.auth_schema import TokenResponse, LoginRequest
from app.features.auth.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Autenticacion"])

@router.post("/login", response_model=TokenResponse)
def login(request : LoginRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login(request.document, request.password)