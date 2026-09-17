from fastapi import APIRouter, Depends, HTTPException, status
from app.models.product import Product
from app.models.category import Category
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate, ProductListResponse


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=ProductListResponse)
def get_products(page: int | None = 1, limit: int | None = 3, db: Session = Depends(get_db)):

    total = db.query(Product).count()

    offset = (page - 1) * limit

    products = db.query(Product).offset(offset).limit(limit).all()

    return {
        "total": total,
        "products": products
    }


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    category = db.get(Category, product.category_id)

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    new_product = Product(**product.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    return product

@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_to_update = db.get(Product, product_id)

    if not product_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    if product.category_id is not None:
        category = db.get(Category, product.category_id)

        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    data = product.model_dump(exclude_unset=True).items()

    for field, value in data:
        setattr(product_to_update, field, value)

    db.commit()
    db.refresh(product_to_update)

    return product_to_update


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_to_delete = db.get(Product, product_id)

    if not product_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    db.delete(product_to_delete)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }



















