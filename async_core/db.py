from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    "sqlite+aiosqlite:///./ProductDB.db"
)

Session_async = async_sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
