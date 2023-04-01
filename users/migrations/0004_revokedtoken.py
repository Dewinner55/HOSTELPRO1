# Generated by Django 4.1.7 on 2023-03-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_customuser_activation_code_delete_emailconfirmation"),
    ]

    operations = [
        migrations.CreateModel(
            name="RevokedToken",
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
                ("token", models.TextField(unique=True)),
            ],
        ),
    ]