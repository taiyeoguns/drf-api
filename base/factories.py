import factory
from base.models import Department, Employee
from faker import Faker

fake = Faker()


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    name = factory.Sequence(lambda n: f"Department {n + 1}")


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    email = factory.LazyAttribute(
        lambda o: f"{o.first_name.lower()}.{o.last_name.lower()}@drf-api.local"
    )
    date_of_birth = factory.LazyFunction(fake.date_of_birth)
    department = factory.SubFactory(DepartmentFactory)
