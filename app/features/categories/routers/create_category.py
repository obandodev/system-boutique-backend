from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.categories.schemas.category_schema import CategoryCreate, CategoryResponse
from app.features.categories.services.category_service import CategoryService
from app.shared.dependencies import require_role

router = APIRouter()

@router.post("/", response_model=CategoryResponse)
def create_category(request : CategoryCreate, db : Session = Depends(get_db), current_user: dict = Depends(require_role("Admin"))):
    service = CategoryService(db)
    return service.create_category(request)