# Generated by Django 5.2 on 2025-05-05 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hall",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("rows", models.PositiveIntegerField()),
                ("seatsPerRow", models.PositiveIntegerField()),
            ],
        ),
    ]
