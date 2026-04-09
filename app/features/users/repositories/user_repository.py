from sqlalchemy.orm import Session
from app.features.users.models.user import User


class UserRepository:
    def __init__(self, db : Session):
        self.db = db
    
    def create(self, name : str, last_name : str, type_document, document : str, username : str, phone : str, email : str, password_hash : str, id_rol : int) -> User:
        user = User(
            name=name,
            last_name=last_name,
            type_document=type_document,
            document=document,
            username=username,
            phone=phone,
            email=email,
            password_hash=password_hash,
            id_rol=id_rol
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update(self, user, data) -> User:
        if data.name is not None:
            user.name = data.name
        if data.last_name is not None:
            user.last_name = data.last_name
        if data.username is not None:
            user.username = data.username
        if data.phone is not None:
            user.phone = data.phone
        if data.email is not None:
            user.email = data.email
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_by_document(self, document : str) ->User:
        return self.db.query(User).filter(User.document == document).first()

    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username(self, username : str) -> User:
        return self.db.query(User).filter(User.username == username).first()
    
    def get_all_users(self) ->list[User]:
        return self.db.query(User).all()
    
    def update_state(self, username : str , state)-> User:
        user = self.get_by_username(username)
        user.state = state
        self.db.commit()
        self.db.refresh(user)
        return user