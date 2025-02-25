import pytest
from rest_framework.test import APIClient


@pytest.fixture(name="api_client")
def fixture_api_client():
    return APIClient()


@pytest.fixture(name="auth_api_client")
def fixture_auth_api_client(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    return api_client
