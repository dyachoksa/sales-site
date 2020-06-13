import random

from django.core.management import BaseCommand
from faker import Faker

from blog.models import Category, Post


class Command(BaseCommand):
    help = "Generates some fake data for blog app"

    def handle(self, *args, **options):
        Faker.seed(11414)
        fake = Faker()

        categories = []
        for name in ["Common", "Marketing", "Social"]:
            category = Category.objects.create(name=name)

            categories.append(category.pk)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created an Category object with id {category.pk}"
                )
            )

        for _ in range(15):
            title = fake.sentence(random.randint(3, 6)).strip(".")
            content = "\n".join(
                map(
                    lambda x: f"<p>{x}</p>",
                    fake.texts(random.randint(3, 6), random.choice([400, 600, 800])),
                )
            )

            post = Post.objects.create(
                title=title, content=content, category_id=random.choice(categories)
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created a Post object with id {post.pk}"
                )
            )
