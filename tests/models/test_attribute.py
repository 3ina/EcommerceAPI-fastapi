from sqlalchemy import Integer, String


def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("attribute")


def test_model_structure_column_data_types(db_inspector):
    table = "attribute"
    columns = {column["name"] : column for column in db_inspector.get_columns(table)}

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["description"]["type"], String)

