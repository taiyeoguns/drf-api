from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from base.filtersets import DepartmentFilterSet, EmployeeFilterSet
from base.models import Department, Employee
from base.serializers import DepartmentSerializer, EmployeeSerializer


class BaseViewSet(ModelViewSet):
    lookup_field = "uuid"
    permission_classes = [IsAuthenticated]


class EmployeeViewSet(BaseViewSet):
    """
    This endpoint presents employees which details such as first name, last name etc.

    Each employee can be part of a department.

    retrieve:
        Returns an employee instance

    list:
        Return all employees, ordered by earliest joined

    create:
        Create a new employee

    delete:
        Remove an existing employee

    partial_update:
        Update one or more fields on an existing employee

    update:
        Update an employee
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilterSet


class DepartmentViewSet(BaseViewSet):
    """
    This endpoint presents departments.

    retrieve:
        Returns an department instance

    list:
        Return all departments, ordered by most recently added

    create:
        Create a new department

    delete:
        Remove an existing department

    partial_update:
        Update one or more fields on an existing department

    update:
        Update an department
    """

    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilterSet

    def get_queryset(self):
        return Department.objects.order_by("-created_at")
