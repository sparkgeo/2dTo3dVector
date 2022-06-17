import pytest

@pytest.fixture(scope='function')
def mock_data():
    return {"Key":"Value"}

