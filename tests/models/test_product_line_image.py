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




