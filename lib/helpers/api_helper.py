import requests
from requests.structures import CaseInsensitiveDict

import config


def get_users():
    return requests.get(build_url("/public/v1/users/"))


def get_user(user_name=None, user_id=None):
    query = {'access-token': config.TOKEN}
    if user_name:
        query.update({'name': user_name})
    elif user_id:
        query.update({'id': user_id})
    else:
        raise ValueError("'user_name' or 'user_id' is not passed.")

    return requests.get(build_url("/public/v1/users"), params=query)


def create_user(user_data):
    return requests.post(build_url("/public/v1/users"), data=user_data.get_user_info_in_json(), headers=build_headers())


def update_user(user_data):
    return requests.patch(build_url("/public/v1/users/{}".format(user_data.id)),
                          data=user_data.get_user_info_in_json(), headers=build_headers())


def delete_user(user_id):
    return requests.delete(build_url("/public/v1/users/{}".format(user_id)), headers=build_headers())


def build_url(endpoint):
    return "{URL}/{endpoint}".format(URL=config.URL, endpoint=endpoint)


def build_headers():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Bearer {}".format(config.TOKEN)
    return headers
