from sqlalchemy import Integer, String


def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table("attribute")


def test_model_structure_column_data_types(db_inspector):
    table = "attribute"
    columns = {column["name"] : column for column in db_inspector.get_columns(table)}

    assert isinstance(columns["id"]["type"], Integer)
    assert isinstance(columns["name"]["type"], String)
    assert isinstance(columns["description"]["type"], String)

def test_model_structure_nullable_constraints(db_inspector):
    table = "attribute"

    columns = db_inspector.get_columns(table)
    expected_nullable = {
        "id" : False,
        "name" : False,
        "description" : True,
    }

    for column in columns:
        column_name = column["name"]
        assert column["nullable"] == expected_nullable.get(column_name, False),f"{column_name} is not nullable"




def test_model_structure_column_constraints(db_inspector):
    table = "attribute"
    constraints = db_inspector.get_check_constraints(table)

    assert any(
        constraint["name"] == "attribute_name_length_check"
        for constraint in constraints
    )


def test_model_structure_column_lengths(db_inspector):
    table = "attribute"
    columns = {column["name"] : column for column in db_inspector.get_columns(table)}

    assert columns["name"]["type"].length == 100
    assert columns["description"]["type"].length == 100


def test_model_structure_unique_constraints(db_inspector):
    table = "attribute"
    constraints = db_inspector.get_unique_constraints(table)

    assert any(
                constraint["name"] == "uq_attribute_name"
                for constraint in constraints
               )