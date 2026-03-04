from sqlalchemy.orm import Session
from app.features.users.models.user import User

class UserRepository:
    def __init__(self, db : Session):
        self.db = db
    
    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()