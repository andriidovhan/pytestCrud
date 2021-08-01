"""Test for user's CRUD requests"""

import pytest

from lib.helpers import api_helper
from lib.model import fake_user


def setup_module():
    """Create user object for the tests."""
    pytest.test_user = fake_user.FakeUser()


def test_users_endpoint_response_with_code_status_200():
    """Check that endpoint is available."""
    response = api_helper.get_users()
    assert response.status_code == 200


def test_able_to_create_a_user():
    """Create a user with fake data."""
    response = api_helper.create_user(pytest.test_user)
    assert response.status_code == 201
    check_user_data_in_response(response.json()["data"])


def test_user_is_really_create():
    """Make sure that the user is really created."""
    response = api_helper.get_user(user_name=pytest.test_user.name)
    assert response.status_code == 200
    response_json_data = response.json()["data"]
    assert len(response_json_data) == 1
    check_user_data_in_response(response_json_data[0])
    pytest.test_user.id = response_json_data[0]['id']


def test_update_the_created_user():
    """Update(user_name) the created user."""
    pytest.test_user.name += "Updated"
    response = api_helper.update_user(pytest.test_user)
    assert response.status_code == 200


def test_user_is_really_updated():
    """Make sure that the user is really updated."""
    response = api_helper.get_user(user_id=pytest.test_user.id)
    check_user_data_in_response(response.json()["data"][0])


def test_delete_the_updated_user():
    """Delete the user."""
    response = api_helper.delete_user(pytest.test_user.id)
    assert response.status_code == 204


def test_user_is_really_deleted():
    """Make sure that the user is really deleted."""
    response = api_helper.get_user(user_id=pytest.test_user.id)
    assert response.status_code == 200
    assert len(response.json()['data']) == 0


def check_user_data_in_response(response_data):
    """Compare user_data from response against object."""
    assert response_data["id"] > 0
    assert response_data["name"] == pytest.test_user.name
    assert response_data["email"] == pytest.test_user.email
    assert response_data["gender"] == pytest.test_user.gender
    assert response_data["status"] == pytest.test_user.status
