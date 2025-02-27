import pytest

from base.factories import EmployeeFactory
from base.models import Employee
from base.serializers import EmployeeSerializer, serialize_model_to_dict


@pytest.mark.django_db
def test_employee_serializer_create():
    employee_data = serialize_model_to_dict(
        EmployeeFactory.build(department__name="Dept")
    )
    serializer = EmployeeSerializer(data=employee_data)
    assert serializer.is_valid() is True

    employee = serializer.create(employee_data)

    emp = Employee.objects.get(pk=employee.id)
    assert emp.id is not None
    assert emp.department.id is not None
    assert emp.department.name == "Dept"


@pytest.mark.django_db
def test_employee_serializer_update():
    employee = EmployeeFactory()

    employee_data = serialize_model_to_dict(EmployeeFactory(department__name="Dept"))
    serializer = EmployeeSerializer(data=employee_data)
    assert serializer.is_valid() is True

    serializer.update(employee, employee_data)

    empdb = Employee.objects.get(pk=employee.id)
    assert empdb.id == employee.id
    assert empdb.department.name == "Dept"
