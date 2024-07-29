from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    "sqlite+aiosqlite:///./ProductDB.db"
)

Session_async = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False)

Base = declarative_base()
