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


def test_model_structure_nullable_constraints(db_inspector):
    table = "product_line"
    columns = db_inspector.get_columns(table)

    expected_nullable  = {
        "id":False,
        "price":False,
        "sku":False,
        "stock_qty":False,
        "is_active":False,
        "order":False,
        "weight": False,
        "created_at":False,
        "product_id":False,

    }

    for column in columns:
        column_name = column["name"]
        assert column["nullable"]  == expected_nullable[column_name],f"column {column_name} is not nullable as expected"


def test_model_structure_column_constraints(db_inspector):
    table = "product_line"
    constraints = db_inspector.get_check_constraints(table)
    assert any(constraint["name"] == "product_line_order_range" for constraint in constraints)
    assert any(constraint["name"] == "product_line_max_price_value" for constraint in constraints)


