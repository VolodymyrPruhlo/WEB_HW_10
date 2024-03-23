# Generated by Django 5.0.3 on 2024-03-22 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Quote",
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
                ("quote", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="authors.author"
                    ),
                ),
                ("tags", models.ManyToManyField(to="quotes.tag")),
            ],
        ),
    ]