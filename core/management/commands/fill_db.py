from django.core.management import call_command
from django.core.management.base import BaseCommand

import factory

from factory import fuzzy

from core.models import Department

BATCH_SIZE = 2000


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'core.Employee'

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    position = factory.Faker('job')
    salary = fuzzy.FuzzyDecimal(10000, 100000, 0)


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command("loaddata", "departments.json")  # Load initial data into db using fixtures

        departments = Department.objects.all()
        for department in departments:
            EmployeeFactory.create_batch(BATCH_SIZE, department=department)
