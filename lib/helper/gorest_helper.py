from lib.libraries.http_library import *

USER_API = '/public-api/users'


def create_user(**kwargs):
    body = json.dumps(kwargs)
    response = custom_post_request(BASE_URL+USER_API, body)
    print(response.json())
    assert response.json()['code'] == 200 or response.json()['code'] == 201, f'Something went wrong\n{response.text}'
    return response.json()['data']['id']


def get_user(user_id):
    response = custom_get_request(f"{BASE_URL+USER_API}/{user_id}")
    print(response.status_code)
    print(response.text)
    assert response.json()['code'] == 200, f'Something went wrong\n{response.text}'
    return response.json()['data']


def get_all_users():
    response = custom_get_request(BASE_URL+USER_API)
    assert response.json()['code'] == 200, f'Something went wrong\n{response.text}'
    return response.json()['data']


def update_user(user_id, **kwargs):
    body = json.dumps(kwargs)
    response = custom_patch_request(f"{BASE_URL+USER_API}/{user_id}", body)
    assert response.json()['code'] == 200, f'Something went wrong\n{response.text}'
    return response.json()['data']


def delete_user(user_id):
    response = custom_delete_request(f"{BASE_URL + USER_API}/{user_id}")
    assert response.json()['code'] == 204, f'Something went wrong\n{response.text}'
    return response.json()['data']


def is_user_exists(user_id):
    response = custom_get_request(f"{BASE_URL + USER_API}/{user_id}")
    if response.json()['code'] == 200:
        return True
    elif response.json()['code'] == 404:
        return False


def is_user_delete(user_id):
    response = custom_get_request(f"{BASE_URL + USER_API}/{user_id}")
    if response.json()['code'] == 404:
        return True
    elif response.json()['code'] == 200:
        return False
