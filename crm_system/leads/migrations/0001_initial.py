# Generated by Django 5.0.7 on 2024-07-22 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lead",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=50)),
                (
                    "ads",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ads.ads"
                    ),
                ),
            ],
        ),
    ]