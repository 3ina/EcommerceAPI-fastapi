from sqlalchemy import Integer, String, Text, Boolean, DateTime,Enum
from sqlalchemy.dialects.postgresql import UUID

def test_model_structure_table_exists(db_inspector):
    assert db_inspector.table_exists("product")


def test_model_structure_column_data_types(db_inspector):
    table = "product"
    columns = {column["name"] : column for column in db_inspector.get_columns(table)}

    assert isinstance(columns["id"]["type"],Integer)
    assert isinstance(columns["pid"]["type"],UUID)
    assert isinstance(columns["name"]["type"],String)
    assert isinstance(columns["slug"]["type"],String)
    assert isinstance(columns["description"]["type"],Text)
    assert isinstance(columns["is_digital"]["type"],Boolean)
    assert isinstance(columns["created_at"]["type"],DateTime)
    assert isinstance(columns["updated_at"]["type"],DateTime)
    assert isinstance(columns["is_active"]["type"],Boolean)
    assert isinstance(columns["stock_status"]["type"],Enum)
    assert isinstance(columns["category_id"]["type"],Integer)
    assert isinstance(columns["seasonal"]["type"],Integer)