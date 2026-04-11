from sqlalchemy.orm import Session
from app.features.categories.models.category import Category

class CategoryRepository:
    def __init__(self, db : Session):
        self.db = db
    
    def create(self, name : str, description : str) -> Category:
        category = Category(
            name=name,
            description=description
        )
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category
    
    def get_all_categories(self) ->list[Category]:
        return self.db.query(Category).all()
