from app.features.categories.repositories.category_repository import CategoryRepository
from app.features.categories.schemas.category_schema import CategoryCreate
from sqlalchemy.orm import Session
from app.features.categories.models.category import Category
from app.features.categories.validators.category_validators import validate_category_name_not_exists


class CategoryService:
    def __init__(self, db: Session):
        self.db = db
        self.category_repository = CategoryRepository(db)
    
    def create_category(self, data : CategoryCreate) -> Category:
        validate_category_name_not_exists(self.db, data.name)
        return self.category_repository.create(
            name=data.name,
            description=data.description
        )
    
    def get_all_categories(self) ->list[Category]:
        return self.category_repository.get_all_categories()