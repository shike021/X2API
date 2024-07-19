# src/db/__init__.py

from .session import SessionLocal, engine

# Create all tables
from .base import Base
Base.metadata.create_all(bind=engine)
