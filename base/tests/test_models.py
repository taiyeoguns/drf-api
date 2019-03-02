import pytest
from mixer.backend.django import mixer
from base.models import Department, Employee
from django.utils import timezone


@pytest.fixture
def department():
    return mixer.blend(Department)


@pytest.mark.django_db
class TestModels:
    def test_department_can_be_created(self):
        department = Department(name="Dept", created_at=timezone.now())
        department.save()

        assert department.id is not None
        assert department.name == "Dept"
        assert department.name in str(department)

    def test_employee_can_be_created(self, department):
        employee = Employee(
            first_name="Fname",
            last_name="Lname",
            email="employee@drfapi.local",
            date_of_birth=timezone.now(),
            department=department,
            created_at=timezone.now(),
        )

        employee.save()

        assert employee.id is not None
        assert isinstance(employee.department, Department)
        assert "Fname" in str(employee)
