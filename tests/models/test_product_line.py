from sqlalchemy import Integer, String, Text, Boolean, DateTime, Enum, Numeric, Float
from sqlalchemy.dialects.postgresql import UUID

def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("product_line")


def test_model_structure_column_data_types(db_inspector):
    table = "product_line"
    columns = {column["name"] : column for column in db_inspector.get_columns(table)}

    assert isinstance(columns["id"]["type"],Integer)
    assert isinstance(columns["price"]["type"],type(Numeric(precision=5,scale=2)))
    assert isinstance(columns["sku"]["type"],UUID)
    assert isinstance(columns["stock_qty"]["type"],Integer)
    assert isinstance(columns["is_active"]["type"],Boolean)
    assert isinstance(columns["order"]["type"],Integer)
    assert isinstance(columns["weight"]["type"],Float)
    assert isinstance(columns["created_at"]["type"],DateTime)
    assert isinstance(columns["product_id"]["type"],Integer)


