# Generated by Django 4.2.3 on 2023-09-21 10:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pybo", "0003_remove_student_student"),
    ]

    operations = [
        migrations.RenameField(
            model_name="class",
            old_name="professor",
            new_name="author",
        ),
    ]
