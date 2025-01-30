from sqlalchemy.types import Integer,String,Boolean

def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("category")


def test_model_structure_column_data_types(db_inspector):
    table = "category"
    columns = { column["name"] : column for column in db_inspector.get_columns(table)}
    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["slug"]["type"], String)
    assert isinstance(columns["is_active"]["type"], Boolean)
    assert isinstance(columns["level"]["type"], Integer)
    assert isinstance(columns["parent_id"]["type"], Integer)

"""
- [ ] Verify nullable or not nullable fields
"""

"""
- [ ] Test columns with specific constraints to ensure they are accurately defined.
"""

"""
- [ ] Verify the correctness of default values for relevant columns.
"""

"""
- [ ] Ensure that column lengths align with defined requirements.
"""

"""
- [ ]  Validate the enforcement of unique constraints for columns requiring unique values.
"""
