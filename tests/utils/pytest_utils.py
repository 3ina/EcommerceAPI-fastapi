from typing import List
import pytest
from _pytest.nodes import Item

def pytest_collection_modifyitems(items : List[Item]):
    for item in items:
        if "model" in item.name:
            item.add_marker(pytest.mark.model)

        if "model_structure" in item.name:
            item.add_marker(pytest.mark.model_structure)
