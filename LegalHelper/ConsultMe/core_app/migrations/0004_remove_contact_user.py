# Generated by Django 5.0.3 on 2024-03-30 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core_app", "0003_contact_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="user",
        ),
    ]