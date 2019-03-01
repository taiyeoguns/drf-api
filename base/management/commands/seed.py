from django.core.management.base import BaseCommand
from base.models import Department, Employee
from mixer.backend.django import mixer


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def _get_user(self):
        fname = mixer.faker.first_name()
        lname = mixer.faker.last_name()
        email = f"{fname}.{lname}@drfapi.local".lower()
        dob = mixer.faker.date()

        return {"fname": fname, "lname": lname, "email": email, "dob": dob}

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

        self.stdout.write("Seeding Departments")

        # set bounds not less than 5 or greater than 100
        if options["num"] < 5:
            options["num"] = 5

        if options["num"] > 100:
            options["num"] = 100

        for i in range(options["num"]):

            if i < round(0.4 * options["num"]) - 1:
                mixer.blend(Department, name=mixer.faker.word().capitalize())

        # seed shifts
        self.stdout.write("Seeding Employees")

        for i in range(options["num"]):

            # seed users
            _user = self._get_user()

            mixer.blend(
                Employee,
                first_name=_user.get("fname"),
                last_name=_user.get("lname"),
                email=_user.get("email"),
                dob=_user.get("dob"),
                department=mixer.SELECT,
            )

        self.stdout.write("Done.")
