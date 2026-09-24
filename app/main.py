from fastapi import FastAPI
from app.routers import categories, products, users
from app.middlewares.logging import log_request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="E-commerce API",
    version="0.1.0",
    description="A simple e-commerce API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(log_request)

app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)