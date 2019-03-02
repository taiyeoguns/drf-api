from rest_framework import routers
from base.viewsets import EmployeeViewSet, DepartmentViewSet

router = routers.DefaultRouter()
router.register("departments", DepartmentViewSet, basename="department")
router.register("employees", EmployeeViewSet)
