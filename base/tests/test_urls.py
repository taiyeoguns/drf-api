import pytest
from django.urls import resolve, reverse
from django.views.generic import RedirectView

from base.viewsets import DepartmentViewSet


@pytest.mark.django_db
class TestUrls:
    def test_home_page_is_redirected_to_api_page(self, rf):
        path = reverse("index")
        request = rf.get(path)
        response = RedirectView.as_view(url="/api")(request)

        assert response.status_code == 302
        assert "api" in response.url

    @pytest.mark.skip
    def test_department_list_page(self, rf, admin_user):
        path = reverse("department-list")
        request = rf.get(path)
        request.user = admin_user
        response = DepartmentViewSet.as_view({"get": "list"})(request)

        assert resolve(path).view_name == "department-list"
        assert response.status_code == 200
