from django.core.management.base import BaseCommand

from base.factories import DepartmentFactory, EmployeeFactory
from base.models import Department, Employee


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def _clear(self):
        self.stdout.write("Clearing data")

        Employee.objects.all().delete()
        Department.objects.all().delete()

    def add_arguments(self, parser):
        parser.add_argument(
            "--num", type=int, default=10, help="Number of items to create"
        )

    def handle(self, *args, **options):
        self._clear()  # clear existing table entries
        self.stdout.write("Starting...")

        # set bounds not less than 5 or greater than 100
        num_items = options["num"]

        num_items = max(num_items, 5)
        num_items = min(num_items, 100)

        self.stdout.write("Seeding Departments")
        DepartmentFactory.create_batch(num_items)

        self.stdout.write("Seeding Employees")
        EmployeeFactory.create_batch(num_items)

        self.stdout.write("Done.")
