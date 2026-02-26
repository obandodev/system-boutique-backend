from sqlalchemy.orm import Session
from app.features.users.repositories.user_repository import UserRepository
from app.features.users.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, db:Session): # Le dice al repositorio lo que tiene que guardar en la db
        self.repository = UserRepository(db)
        
    def get_all_users(self):
        return self.repository.get_all()

    def create_user(self, user: UserCreate): # Recibe la request y le envia los datos al repo y tambien hace el response en el router
        return self.repository.create(user)