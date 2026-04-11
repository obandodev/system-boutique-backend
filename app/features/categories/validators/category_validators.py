from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.features.categories.models.category import Category

def validate_category_name_not_exists(db : Session, name : str):
    category = db.query(Category).filter(Category.name ==name).first()
    if category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La categoria '{name} ya existe"
        )