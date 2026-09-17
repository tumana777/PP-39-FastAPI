from fastapi import APIRouter, Depends, HTTPException, status
from app.models.product import Product
from app.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products