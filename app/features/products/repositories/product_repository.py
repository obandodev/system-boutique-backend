from sqlalchemy.orm import Session
from app.features.products.models.product import Product
from app.features.products.schemas.product_schema import ProductCreate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, product : ProductCreate):
        new_product = Product(
            codigo = product.codigo,
            name = product.name,
            color = product.color,
            marca = product.marca
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product