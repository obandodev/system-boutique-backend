from sqlalchemy.orm import Session
from app.features.users.models.user import User
from app.features.users.schemas.user_schema import UserCreate, UserRegister
from app.features.users.repositories.user_repository import UserRepository
from app.features.users.validators.user_validators import (validate_email_not_exists, validate_document_not_exists, validate_username_not_exists, validate_role_exists, validate_role_active)
from app.shared.security import hashed_password

class UserService:
    def __init__(self, db : Session):
        self.db = db
        self.user_repository = UserRepository(db)
    
    def create_user(self, data: UserCreate) -> User: # Registros hechos por el Admin
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
    
    def register_user(self, data: UserRegister) -> User: # Registros de Clientes
        validate_email_not_exists(self.db, data.email)
        validate_document_not_exists(self.db, data.document)
        validate_username_not_exists(self.db, data.username)
        role = validate_role_exists(self.db, 3)
        validate_role_active(role, 3)
        return self.user_repository.create(
            name=data.name,
            last_name=data.last_name,
            type_document=data.type_document,
            document=data.document,
            username=data.username,
            phone=data.phone,
            email=data.email,
            password_hash=hashed_password(data.password),
            id_rol=3 # Id del rol del cliente desde postgres
        )

    def get_all_users(self) ->list[User]:
        return self.user_repository.get_all_users()