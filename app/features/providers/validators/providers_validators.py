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