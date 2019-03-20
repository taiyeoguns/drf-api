from rest_framework.viewsets import ModelViewSet
from base.models import Employee, Department
from base.serializers import EmployeeSerializer, DepartmentSerializer
from base.filtersets import EmployeeFilterSet, DepartmentFilterSet


class EmployeeViewSet(ModelViewSet):
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
    lookup_field = "uuid"


class DepartmentViewSet(ModelViewSet):
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
    lookup_field = "uuid"

    def get_queryset(self):
        return Department.objects.order_by("-created_at")
