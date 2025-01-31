from .db_connection import Base

from sqlalchemy import (
    Column,
    INTEGER,
    String, Boolean, Integer, ForeignKey
)

class Category(Base):
    __tablename__ = "category"
    id = Column(INTEGER, primary_key=True,nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(120), nullable=False)
    is_active = Column(Boolean, nullable=False)
    level = Column(Integer,nullable=False)
    parent_id = Column(Integer,nullable=True)
