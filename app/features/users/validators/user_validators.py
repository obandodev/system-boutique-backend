from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.features.users.models.user import User
from app.features.roles.models.rol import Role, StateRolType

def validate_email_not_exists(db : Session, email : str): 
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El email '{email}' ya esta registrado"
        )

def validate_document_not_exists(db : Session, document : str): 
    user = db.query(User).filter(User.document == document).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El documento '{document}' ya esta registrado"
        )

def validate_username_not_exists(db : Session, username : str): 
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El usuario '{username}' ya esta registrado"
        )
    
def validate_role_exists(db : Session, id_rol : int):
    role = db.query(Role).filter(Role.id_rol == id_rol).first()
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El rol con id '{id_rol}' no existe"
        )
    return role

def validate_role_active(role : Role, id_rol : int): 
    if role.state != StateRolType.Active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El rol con id '{id_rol}' esta inactivo"
        )
    
def validate_username_exists(existing_username, username : str):
    if not existing_username:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El username '{username}' no existe"
        )

def validate_username_not_exists_for_update(db: Session, username: str, id_user: int):
    user = db.query(User).filter(User.username == username, User.id_user != id_user).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El username '{username}' ya esta registrado"
        )

def validate_email_not_exists_for_update(db: Session, email: str, id_user: int):
    user = db.query(User).filter(User.email == email, User.id_user != id_user).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El email '{email}' ya esta registrado"
        )

def validate_phone_not_exists_for_update(db: Session, phone: str, id_user: int):
    user = db.query(User).filter(User.phone == phone, User.id_user != id_user).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El phone '{phone}' ya esta registrado"
        )