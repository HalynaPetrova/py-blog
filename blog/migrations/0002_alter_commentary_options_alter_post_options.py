# Generated by Django 4.2.5 on 2023-09-24 11:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={"ordering": ("-created_time",)},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("-created_time",)},
        ),
    ]