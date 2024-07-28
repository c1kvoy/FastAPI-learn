from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///./ProductDB.db"
)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
