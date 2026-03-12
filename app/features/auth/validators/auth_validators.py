from fastapi import HTTPException, status
from app.features.users.models.user import StateUserType
from app.shared.security import verify_password

def validate_user_exists(user):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales Incorrectas"
        )

def validate_password(password: str, password_hash: str):
    if not verify_password(password, password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales Incorrectas"
        )

def validate_user_active(user):
    if user.state != StateUserType.Active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario Inactivo"
        )