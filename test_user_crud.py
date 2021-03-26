from lib.helper.gorest_helper import *


class TestCrud:
    def test_create_user(self, create_test_user):
        user_id = create_test_user
        assert is_user_exists(user_id)

    def test_update_user_name(self, create_test_user):
        user_id = create_test_user
        assert get_user(user_id)['name'] == "Test User"
        update_user(user_id, name="New Test User", gender="Male", email="my@mail.com", status="Active")
        assert get_user(user_id)['name'] == "New Test User"
