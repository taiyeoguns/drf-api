from rest_framework.serializers import HyperlinkedModelSerializer
from base.models import Employee, Department


class DepartmentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ("id", "url", "name", "created_at")


class EmployeeSerializer(HyperlinkedModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = (
            "id",
            "url",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "department",
            "created_at",
        )
