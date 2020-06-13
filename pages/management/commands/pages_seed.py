import random

from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.core.management import BaseCommand
from faker import Faker

from pages.models import Employee


class Command(BaseCommand):
    help = "Generates some fake data for pages app"

    def handle(self, *args, **options):
        Faker.seed(1212)
        fake = Faker()

        for _ in range(6):
            profile = fake.profile()

            employee = Employee.objects.create(
                name=profile["name"],
                position=profile["job"],
                description=profile["company"],
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created an Employee object with id {employee.pk}"
                )
            )

        site = Site.objects.get_current()

        for _ in range(4):
            title = fake.sentence(random.randint(3, 6)).strip(".")
            content = "\n".join(
                map(
                    lambda x: f"<p>{x}</p>",
                    fake.texts(random.randint(3, 6), random.choice([400, 600, 800])),
                )
            )

            page = FlatPage.objects.create(
                url="/pages/{}/".format(fake.uri_page()), title=title, content=content
            )
            page.sites.add(site)
            page.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created a FlatPage object with id {page.pk}"
                )
            )
