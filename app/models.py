from .db_connection import Base

from sqlalchemy import (
    Column,
    INTEGER,
    String, Boolean, Integer, ForeignKey
)

class Category(Base):
    __tablename__ = "category"
    id = Column(INTEGER, primary_key=True)
    name = Column(String(100))
    slug = Column(String(120))
    is_active = Column(Boolean)
    level = Column(Integer)
    parent_id = Column(Integer)
