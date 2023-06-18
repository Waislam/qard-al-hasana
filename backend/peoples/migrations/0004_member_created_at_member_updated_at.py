# Generated by Django 4.1.2 on 2023-06-18 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("peoples", "0003_remove_staff_branch_remove_staff_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
