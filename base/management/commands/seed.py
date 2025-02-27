import uuid

import factory
from decouple import config
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

from base.factories import DepartmentFactory, EmployeeFactory
from base.models import Department, Employee


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def _clear(self):
        self.stdout.write("Clearing data")

        get_user_model().objects.all().delete()
        Token.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

    def add_arguments(self, parser):
        parser.add_argument(
            "--num", type=int, default=10, help="Number of items to create"
        )

    def handle(self, *args, **options):
        self._clear()  # clear existing table entries
        self.stdout.write("Starting...")
        admin_user = get_user_model().objects.create_superuser(
            "admin",
            f"admin@{config('APP_DOMAIN')}",
            config("DEFAULT_ADMIN_PASSWORD"),
            first_name="Admin",
            last_name="User",
        )
        token = Token.objects.create(
            user=admin_user, key=config("DEFAULT_ADMIN_TOKEN", uuid.uuid4().hex)
        )

        # set bounds not less than 5 or greater than 100
        num_items = options["num"]

        num_items = max(num_items, 5)
        num_items = min(num_items, 100)

        num_departments = max(1, int(num_items * 0.2))  # Ensure at least 1 department

        departments = DepartmentFactory.create_batch(num_departments)
        self.stdout.write(f"Seeded {num_departments} Departments")

        EmployeeFactory.create_batch(
            num_items, department=factory.Iterator(departments)
        )
        self.stdout.write(f"Seeded {num_items} Employees")

        self.stdout.write("Done.")
        self.stdout.write(f"Admin user created with API key: {token.key}")
