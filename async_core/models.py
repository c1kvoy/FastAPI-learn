from .db import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_name: Mapped[str | None] = mapped_column(nullable=True, index=True)
    description: Mapped[str | None] = mapped_column(nullable=True)

    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="product")


class Transaction(Base):
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    count: Mapped[int] = mapped_column(nullable=True)

    product: Mapped["Product"] = relationship("Product", back_populates="transactions")
