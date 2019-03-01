from rest_framework.serializers import ModelSerializer
from base.models import Employee, Department


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ("id", "name")


class EmployeeSerializer(ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "email", "date_of_birth", "department")
