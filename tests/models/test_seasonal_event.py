from sqlalchemy import DateTime, Integer, String


def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("seasonal_event")


def test_model_structure_column_data_types(db_inspector):
    table = "seasonal_event"
    columns = {column["name"]: column for column in db_inspector.get_columns(table)}

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["start_date"]["type"], DateTime)
    assert isinstance(columns["end_date"]["type"], DateTime)
    assert isinstance(columns["name"]["type"], String)
