from sqlalchemy.orm import Session
from app.features.products.repositories.product_repository import ProductRepository
from app.features.products.schemas.product_schema import ProductCreate

class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)
    
    def create_product(self, product: ProductCreate):
        return self.repository.create(product)