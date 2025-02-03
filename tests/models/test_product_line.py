from sqlalchemy import Integer, String, Text, Boolean, DateTime,Enum
from sqlalchemy.dialects.postgresql import UUID

def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("product_line")


