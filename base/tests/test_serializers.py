from base.serializers import EmployeeSerializer
from mixer.backend.django import mixer
from base.models import Employee
import pytest


@pytest.mark.django_db
def test_employee_serializer_create():
    data = {
        "first_name": "First",
        "last_name": mixer.faker.last_name(),
        "email": mixer.faker.email(),
        "date_of_birth": mixer.faker.date(),
        "department": {"name": "Dept"},
    }

    serializer = EmployeeSerializer(data=data)
    assert serializer.is_valid() is True

    employee = serializer.create(data)

    emp = Employee.objects.get(pk=employee.id)
    assert emp.id is not None
    assert emp.department.id is not None
    assert emp.department.name == "Dept"


@pytest.mark.django_db
def test_employee_serializer_update():

    emp1 = mixer.blend(Employee)

    data = {
        "first_name": "First",
        "last_name": mixer.faker.last_name(),
        "email": mixer.faker.email(),
        "date_of_birth": mixer.faker.date(),
        "department": {"name": "Dept"},
    }

    serializer = EmployeeSerializer(data=data)
    assert serializer.is_valid() is True

    serializer.update(emp1, data)

    empdb = Employee.objects.get(pk=emp1.id)
    assert empdb.id == emp1.id
    assert empdb.department.name == "Dept"
