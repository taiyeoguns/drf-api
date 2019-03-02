from rest_framework.viewsets import ModelViewSet
from base.models import Employee, Department
from base.serializers import EmployeeSerializer, DepartmentSerializer
from base.filtersets import EmployeeFilterSet, DepartmentFilterSet


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilterSet


class DepartmentViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilterSet

    def get_queryset(self):
        return Department.objects.order_by("-created_at")
