from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize


def upload_to(instance: "Employee", filename):
    name_slug = slugify(instance.name)
    return "employees/{}/{}".format(name_slug, filename)


class Employee(models.Model):
    name = models.CharField("employee name", max_length=150, null=False, blank=False)
    position = models.CharField("employee position", max_length=150)
    description = models.TextField("extra information")
    photo = models.ImageField(
        "employee photo", upload_to=upload_to, blank=True, null=True
    )

    photo_80x80 = ImageSpecField(
        source="photo",
        processors=[SmartResize(80, 80)],
        format="JPEG",
        options={"quality": 80},
    )
    photo_300x200 = ImageSpecField(
        source="photo",
        processors=[SmartResize(300, 200)],
        format="JPEG",
        options={"quality": 80},
    )

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Employee id={self.pk} name={self.name} position={self.position}>"
