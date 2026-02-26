from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.features.products.services.product_service import ProductService
from app.features.products.schemas.product_schema import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductResponse)
def create_product(product : ProductCreate, db: Session= Depends(get_db)):
    service = ProductService(db)
    return service.create_product(product)