from ckeditor.fields import RichTextField
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category id={self.pk} name={self.name}>"


class Post(models.Model):
    title = models.CharField(max_length=150, null=False)
    slug = AutoSlugField(unique=True, populate_from='title')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = RichTextField(null=False, blank=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Post id={self.pk} title={self.title}>"
