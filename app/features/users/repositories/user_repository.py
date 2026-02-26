from sqlalchemy.orm import Session
from app.features.users.models.user import User
from app.features.users.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(User).all()
    
    def create(self, user:UserCreate):
        new_user = User(
            name= user.name,
            email= user.email,
            password= user.password
        )
        self.db.add(new_user) # Le decimos a la db que tenga el new user
        self.db.commit() # Ejecutamos la nueva request para guardarlo en el db
        self.db.refresh(new_user) # Actualice el objeto con los datos que creo postgres  automaticamente ej: id, created_at
        return new_user # devuelve el nuevo usuario