def test_model_structure_table_exists(db_inspector):
    assert db_inspector.table_exists("product")

