from sqlalchemy import Integer, String



def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("product_image")





def test_model_structure_column_data_types(db_inspector):
    table = "product_image"
    columns = {columns["name"]: columns for columns in db_inspector.get_columns(table)}

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["alternative_text"]["type"], String)
    assert isinstance(columns["url"]["type"], String)
    assert isinstance(columns["order"]["type"], Integer)
    assert isinstance(columns["product_line_id"]["type"], Integer)





def test_model_structure_nullable_constraints(db_inspector):
    table = "product_image"
    columns = db_inspector.get_columns(table)

    expected_nullable = {
        "id": False,
        "alternative_text": False,
        "url": False,
        "order": False,
        "product_line_id": False,
    }

    for column in columns:
        column_name = column["name"]
        assert column["nullable"] == expected_nullable.get(
            column_name
        ), f"column '{column_name}' is not nullable as expected"


