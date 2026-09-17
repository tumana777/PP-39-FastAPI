from pydantic import BaseModel

class ProductInCategory(BaseModel):
    id: int
    name: str

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    products: list[ProductInCategory]