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
    assert isinstance(columns["seasonal_event"]["type"],Integer)


def test_model_structure_nullable_constraints(db_inspector):
    table = "product"
    columns = db_inspector.get_columns(table)

    expected_nullable  = {
        "id":False,
        "pid":False,
        "name":False,
        "slug":False,
        "description":True,
        "is_digital":False,
        "created_at":False,
        "updated_at":False,
        "is_active":False,
        "stock_status":False,
        "category_id":False,
        "seasonal_event":True,

    }

    for column in columns:
        column_name = column["name"]
        assert column["nullable"]  == expected_nullable[column_name],,f"column {column_name} is not nullable as expected"

