from django_filters.rest_framework import FilterSet
from base.models import Department, Employee


class EmployeeFilterSet(FilterSet):
    class Meta:
        model = Employee
        fields = {
            "first_name": ["icontains"],
            "last_name": ["icontains"],
            "email": ["iexact"],
            "date_of_birth": ["year__lte", "year__gte"],
            "created_at": ["year__lte", "year__gte"],
        }


class DepartmentFilterSet(FilterSet):
    class Meta:
        model = Department
        fields = {"name": ["icontains"], "created_at": ["year__lte", "year__gte"]}
