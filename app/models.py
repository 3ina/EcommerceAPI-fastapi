from .db_connection import Base

from sqlalchemy import (
    Column,
    INTEGER
)

class Category(Base):
    __tablename__ = "category"
    id = Column(INTEGER, primary_key=True)