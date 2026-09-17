from pydantic import BaseModel, Field
from datetime import datetime


class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=255)
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)
    category_id: int = Field(gt=0)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    is_available: bool
    created_at: datetime
    updated_at: datetime
    category_id: int

class ProductListResponse(BaseModel):
    total: int
    products: list[ProductResponse]

class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=255)
    price: float | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, gt=0)
    is_available: bool | None = Field(default=True)
    category_id: int | None = Field(default=None, gt=0)