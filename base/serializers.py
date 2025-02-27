from django.db.models import Model
from rest_framework.serializers import HyperlinkedModelSerializer, ReadOnlyField

from base.models import Department, Employee


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


# https://blog.okello.io/tutorials/recursively-convert-django-model-to-dict/
def serialize_model_to_dict(model: Model, fields: dict = None) -> dict:
    if not fields:
        fields = {
            field.name: getattr(model, field.name) for field in model._meta.fields
        }
    for field_name, field_value in fields.items():
        if not isinstance(field_value, Model):
            # skip non-relational (ForeignKey) fields
            continue
        fields[field_name] = serialize_model_to_dict(field_value)
    return fields
