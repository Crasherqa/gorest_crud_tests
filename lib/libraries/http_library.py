import requests
import json

TOKEN = "de3e1e42cf964d4adf072139e24324b2e78af2025ff354c00ef5e8875943a8f0"
BASE_URL = "https://gorest.co.in"
HEADER = {'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + TOKEN
          }
TIMEOUT = 20


def custom_get_request(url):
    """
    :param url: Request URL
    :return: Request response
    """
    return requests.get(url=url, timeout=TIMEOUT, headers=HEADER)


def custom_post_request(url, request_body=None):
    """
    :param url: Request URL
    :param request_body: post body
    :return: Request response
    """
    return requests.post(url=url, timeout=TIMEOUT, headers=HEADER, data=request_body)


def custom_put_request(url, request_body=None):
    """
    :param url: Request URL
    :param request_body: post body
    :return: Request response
    """
    return requests.put(url=url, timeout=TIMEOUT, headers=HEADER, data=request_body)


def custom_patch_request(url, request_body=None):
    """
    :param url: Request URL
    :param request_body: post body
    :return: Request response
    """
    return requests.patch(url=url, timeout=TIMEOUT, headers=HEADER, data=request_body)


def custom_delete_request(url, request_body=None):
    """
    :param url: Request URL
    :param request_body: delete body
    :return: Request response
    """
    return requests.delete(url=url, timeout=TIMEOUT, headers=HEADER, data=request_body)
