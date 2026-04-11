from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.categories.schemas.category_schema import CategoryCreate, CategoryResponse
from app.features.categories.services.category_service import CategoryService
from app.shared.dependencies import require_role

router = APIRouter()

@router.get("/", response_model=list[CategoryResponse], dependencies=[Depends(require_role("Admin"))])
def get_all_categories(db : Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_all_categories()