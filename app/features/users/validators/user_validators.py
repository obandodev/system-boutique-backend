from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.features.users.models.user import User
from app.features.roles.models.rol import Role, StateRolType

def validate_email_not_exists(db : Session, email : str): # UserCreate y UserRegister - valida que el email no esté registrado
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El email '{email}' ya esta registrado"
        )

def validate_document_not_exists(db : Session, document : str): # UserCreate y UserRegister - valida que el documento no esté registrado
    user = db.query(User).filter(User.document == document).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El documento '{document}' ya esta registrado"
        )

def validate_username_not_exists(db : Session, username : str): # UserCreate y UserRegister - valida que el usuario no esté registrado
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El usuario '{username}' ya esta registrado"
        )
    
def validate_role_exists(db : Session, id_rol : int): # Solo UserCreate (Admin) - valida que el rol exista
    role = db.query(Role).filter(Role.id_rol == id_rol).first()
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El rol con id '{id_rol}' no existe"
        )
    return role

def validate_role_active(role : Role, id_rol : int): # Solo UserCreate (Admin) - valida que el rol se encuentre activo
    if role.state != StateRolType.Active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El rol con id '{id_rol}' esta inactivo"
        )
    
def validate_username_exists(existing_role, username : str):
    if not existing_role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El username '{username}' no existe"
        )