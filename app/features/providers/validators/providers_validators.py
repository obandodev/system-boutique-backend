from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.features.providers.models.provider import Provider

def validate_provider_name_not_exists(db : Session, name: str):
    provider = db.query(Provider).filter(Provider.name==name).first()
    if provider:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El proveedor '{name}' ya existe"
        )

def validate_provider_name_exists(existing_name_provider, name: str):
    if not existing_name_provider:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El proveedor '{name}' no existe"
        )

def validate_provider_name_not_exists_for_update(db: Session, name: str, id_provider: int):
    provider = db.query(Provider).filter(Provider.name == name, Provider.id_provider != id_provider).first()
    if provider:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El proveedor '{name}' ya esta registrado"
        )

def validate_provider_exists(provider, id_provider: int):
    if not provider:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El proveedor con id '{id_provider}' no existe"
        )