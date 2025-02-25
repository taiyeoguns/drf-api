import pytest
from rest_framework import status
from rest_framework.authtoken.models import Token

from base.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_unauthenticated_access(api_client):
    response = api_client.get("/api/employees/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_authenticated_access(auth_api_client):
    response = auth_api_client.get("/api/employees/")
    assert response.status_code == status.HTTP_200_OK


def test_authenticated_access_x_api_key_header(api_client):
    token = "00000000-0000-0000-0000-000000000000"
    Token.objects.create(user=UserFactory(), key=token)

    response = api_client.get("/api/employees/", headers={"X-API-KEY": token})
    assert response.status_code == status.HTTP_200_OK
