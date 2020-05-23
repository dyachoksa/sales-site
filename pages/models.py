from django.db import models


class Employee(models.Model):
    name = models.CharField("employee name", max_length=150, null=False, blank=False)
    position = models.CharField("employee position", max_length=150)
    description = models.TextField("extra information")

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Employee id={self.pk} name={self.name} position={self.position}>"
