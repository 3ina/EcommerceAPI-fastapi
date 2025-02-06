from sqlalchemy import Integer,String

def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("product_type")


def test_model_structure_column_data_types(db_inspector):
    table = "product_type"
    columns = {column["name"]: column for column in db_inspector.get_columns(table)}

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["level"]["type"], Integer)
    assert isinstance(columns["parent_id"]["type"], Integer)
