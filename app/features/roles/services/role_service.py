from sqlalchemy.orm import Session
from app.features.roles.repositories.role_repository import RoleRepository
from app.features.roles.models.rol import  StateRolType
from app.features.roles.models.rol import Role
from app.features.roles.validators.roles_validators import (validate_role_exists , validate_role_not_exists, validate_role_access)


class RoleService:
    def __init__(self, db : Session):
        self.db = db
        self.role_repository = RoleRepository(db)
    
    def create_role(self , name_rol : str) -> Role:
        existing_role = self.role_repository.get_by_name(name_rol)
        validate_role_not_exists(existing_role, name_rol)
        return self.role_repository.create(name_rol)
    
    def update_role(self, name_rol: str) -> Role:
        existing_role = self.role_repository.get_by_name(name_rol)
        validate_role_exists(existing_role, name_rol)
        new_state = StateRolType.Inactive if existing_role.state == StateRolType.Active else StateRolType.Active
        return self.role_repository.update_state(name_rol , new_state)
    
    def get_all_roles(self) ->list[Role]:
        return self.role_repository.get_all_roles()
    
    def get_role_by_name(self, name_rol: str, current_user: dict) -> Role:
        validate_role_access(current_user, name_rol)
        existing_role = self.role_repository.get_by_name(name_rol)
        validate_role_exists(existing_role, name_rol)
        return existing_role