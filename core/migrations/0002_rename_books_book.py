# Generated by Django 4.1.6 on 2023-02-13 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Books",
            new_name="Book",
        ),
    ]
