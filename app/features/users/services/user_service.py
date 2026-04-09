from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.features.users.models.user import User
from app.features.users.schemas.user_schema import UserCreate, UserUpdate
from app.features.users.repositories.user_repository import UserRepository
from app.features.users.models.user import StateUserType
from app.features.users.validators.user_validators import (validate_email_not_exists, validate_document_not_exists, validate_username_not_exists, validate_role_exists, validate_role_active, validate_username_exists, validate_email_not_exists_for_update, validate_phone_not_exists_for_update, validate_username_not_exists_for_update)
from app.shared.security import hashed_password

class UserService:
    def __init__(self, db : Session):
        self.db = db
        self.user_repository = UserRepository(db)
    
    def create_user(self, data: UserCreate) -> User: 
        validate_email_not_exists(self.db, data.email)
        validate_document_not_exists(self.db, data.document)
        validate_username_not_exists(self.db, data.username)
        role = validate_role_exists(self.db, data.id_rol)
        validate_role_active(role, data.id_rol)
        return self.user_repository.create(
            name=data.name,
            last_name=data.last_name,
            type_document=data.type_document,
            document=data.document,
            username=data.username,
            phone=data.phone,
            email=data.email,
            password_hash=hashed_password(data.password),
            id_rol=data.id_rol
        )
    
    def update_user_info(self, document: str, data: UserUpdate, current_user: dict) -> User:
        user = self.user_repository.get_by_document(document)
        validate_username_exists(user, document)
        if current_user.get("role") != "Admin":
            if current_user.get("sub") != user.document:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Acceso denegado, no tienes los permisos suficientes"
                )
        if data.username is not None:
            validate_username_not_exists_for_update(self.db, data.username, user.id_user)
        if data.email is not None:
            validate_email_not_exists_for_update(self.db, data.email, user.id_user)
        if data.phone is not None:
            validate_phone_not_exists_for_update(self.db, data.phone, user.id_user)
        return self.user_repository.update(user, data)
    
    def get_user_by_document(self, document: str) -> User:
        user = self.user_repository.get_by_document(document)
        validate_username_exists(user, document)
        return user

    def get_all_users(self) ->list[User]:
        return self.user_repository.get_all_users()

    def update_user(self, username : str) -> User:
        existing_user = self.user_repository.get_by_username(username)
        validate_username_exists(existing_user, username)
        new_state = StateUserType.Inactive if existing_user.state == StateUserType.Active else StateUserType.Active
        return self.user_repository.update_state(username, new_state)
    
    def get_my_profile(self, email : str) -> User:
        user = self.user_repository.get_by_email(email)
        validate_username_exists(user, email)
        return user
