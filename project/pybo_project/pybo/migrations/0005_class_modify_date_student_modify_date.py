# Generated by Django 4.2.3 on 2023-10-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pybo", "0004_rename_professor_class_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
