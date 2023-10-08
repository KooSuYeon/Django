# Generated by Django 4.2.3 on 2023-09-17 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Class",
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
                ("subject", models.CharField(max_length=200)),
                ("class_info", models.TextField()),
                ("create_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("student_code", models.TextField()),
                ("create_date", models.DateTimeField()),
                (
                    "_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pybo.class"
                    ),
                ),
            ],
        ),
    ]
