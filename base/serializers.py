from rest_framework.serializers import HyperlinkedModelSerializer, ReadOnlyField
from base.models import Employee, Department


class DepartmentSerializer(HyperlinkedModelSerializer):
    id = ReadOnlyField(source="uuid")

    class Meta:
        model = Department
        extra_kwargs = {"url": {"lookup_field": "uuid"}}
        fields = ("id", "url", "name", "created_at")


class EmployeeSerializer(HyperlinkedModelSerializer):
    id = ReadOnlyField(source="uuid")
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        extra_kwargs = {"url": {"lookup_field": "uuid"}}
        fields = (
            "id",
            "url",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "created_at",
            "department",
        )

    def create(self, validated_data):
        dept_data = validated_data.pop("department")
        department = Department.objects.create(**dept_data)
        return Employee.objects.create(department=department, **validated_data)

    def update(self, instance, validated_data):

        if "department" in validated_data:
            dept_data = validated_data.pop("department")
            instance.department.name = dept_data.get("name", instance.department.name)
            instance.department.save()

        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )

        instance.save()

        return instance
