import pytest


@pytest.fixture
def updated_test_lot_data(test_lot_data):
    test_lot_data["name"] += "_updated"
    test_lot_data["description"] += "_updated"

    return test_lot_data
