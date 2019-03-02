from django.urls import reverse, resolve
from django.test import RequestFactory
import pytest
from base.viewsets import DepartmentViewSet
from django.views.generic import RedirectView


@pytest.fixture(scope="module")
def factory():
    return RequestFactory()


@pytest.mark.django_db
class TestUrls:
    def test_home_page_is_redirected_to_api_page(self, factory):
        path = reverse("index")
        request = factory.get(path)
        response = RedirectView.as_view(url="/api")(request)

        assert response.status_code == 302
        assert "api" in response.url

    def test_department_list_page(self, factory):
        path = reverse("department-list")
        request = factory.get(path)
        response = DepartmentViewSet.as_view({"get": "list"})(request)

        assert resolve(path).view_name == "department-list"
        assert response.status_code == 200
