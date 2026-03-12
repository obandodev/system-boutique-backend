from sqlalchemy.orm import Session
from app.features.roles.models.rol import Role

class RoleRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, name_rol : str) -> Role:
        role = Role(name_rol=name_rol)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role
    
    def get_by_name(self, name_rol: str) -> Role:
        return self.db.query(Role).filter(Role.name_rol==name_rol).first()
    
    def get_all_roles(self) -> list[Role]:
        return self.db.query(Role).all()
    
    def update_state(self, name_rol : str, state) -> Role:
        role = self.get_by_name(name_rol)
        role.state = state
        self.db.commit()
        self.db.refresh(role)
        return role