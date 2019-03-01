from django.urls import path, include
from rest_framework import routers
from base.viewsets import EmployeeViewSet, DepartmentViewSet

router = routers.DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("employees", EmployeeViewSet)

urlpatterns = [path("", include(router.urls))]

