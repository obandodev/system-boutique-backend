from sqlalchemy.orm import Session
from app.features.users.repositories.user_repository import UserRepository
from app.shared.security import create_access_token
from app.features.auth.validators.auth_validators import (validate_user_exists, validate_password, validate_user_active )


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def login(self, email:str, password:str) -> dict:
        user = self.user_repository.get_by_email(email)

        validate_user_exists(user)
        validate_password(password, user.password_hash)
        validate_user_active(user)
        
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