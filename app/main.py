from fastapi import FastAPI
from app.routers import categories, products

app = FastAPI(
    title="E-commerce API",
    version="0.1.0",
    description="A simple e-commerce API",
)

app.include_router(categories.router)
app.include_router(products.router)