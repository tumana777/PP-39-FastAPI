from app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    products: Mapped[list["Product"]] = relationship(back_populates="category", cascade="all, delete")

    def __str__(self):
        return self.name