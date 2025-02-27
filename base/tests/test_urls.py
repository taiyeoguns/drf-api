import pytest
from django.urls import resolve, reverse
from django.views.generic import RedirectView
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_home_page_is_redirected_to_api_page(rf):
    path = reverse("index")
    request = rf.get(path)
    response = RedirectView.as_view(url="/api")(request)

    assert response.status_code == status.HTTP_302_FOUND
    assert "api" in response.url


def test_department_list_page(auth_api_client):
    path = reverse("department-list")

    response = auth_api_client.get(path)

    assert resolve(path).view_name == "department-list"
    assert response.status_code == status.HTTP_200_OK
