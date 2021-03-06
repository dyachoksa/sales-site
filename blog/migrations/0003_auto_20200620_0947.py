# Generated by Django 3.0.7 on 2020-06-20 09:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20200613_0735"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content_en",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="content_ru",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="content_uk",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="title_en",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="title_ru",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="title_uk",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
