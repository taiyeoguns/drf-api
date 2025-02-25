import factory
from decouple import config
from django.conf import settings
from django.contrib.auth import get_user_model
from faker import Faker

from base.models import Department, Employee

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)

    @factory.lazy_attribute
    def username(self):
        return f"{self.first_name}.{self.last_name}".lower()

    @factory.lazy_attribute
    def email(self):
        return f"{self.username}@{config('APP_DOMAIN')}"


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
        lambda o: f"{o.first_name.lower()}.{o.last_name.lower()}@{settings.APP_DOMAIN}"
    )
    date_of_birth = factory.LazyFunction(fake.date_of_birth)
    department = factory.SubFactory(DepartmentFactory)
