import pytest
from lib.helper.gorest_helper import *


@pytest.fixture
def create_test_user():
    user_id = create_user(name="Test User", gender="Male", email="my@mail.com", status="Active")
    yield user_id
    delete_user(user_id)
