from .db import Base
from sqlalchemy.orm import mapped_column, Mapped
class Product(Base):
    __tablename__ = 'products'

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    product_name: Mapped[str | None] = mapped_column(nullable=True, index=True)
    description: Mapped[str | None] = mapped_column(nullable=True)

