from sqlalchemy.orm import Session
from app.features.users.repositories.user_repository import UserRepository
from app.shared.security import verify_password, create_access_token
from app.features.users.models.user import StateUserType
from fastapi import HTTPException, status

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)


    def login(self, email:str, password:str) -> dict:
        user = self.user_repository.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Credenciales Incorrectas")

        if not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales Incorrectas")
        
        if user.state !=  StateUserType.Active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario Inactivo"
            )
        
        token = create_access_token({
            "sub" : user.email,
            "role" : user.role.name_rol,
            "user_id" : user.id_user
        })

        return {
            "access_token" : token,
            "token_type" : "bearer",
            "role" : user.role.name_rol
        }