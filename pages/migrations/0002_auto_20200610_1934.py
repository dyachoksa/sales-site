# Generated by Django 3.0.7 on 2020-06-10 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('id',)},
        ),
    ]
