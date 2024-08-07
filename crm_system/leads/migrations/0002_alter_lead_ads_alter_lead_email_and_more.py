# Generated by Django 5.0.7 on 2024-07-23 12:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
        ("leads", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="ads",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ads.ads",
                verbose_name="Рекламная компания, из которой узнал об услуге",
            ),
        ),
        migrations.AlterField(
            model_name="lead",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Электронная почта"),
        ),
        migrations.AlterField(
            model_name="lead",
            name="first_name",
            field=models.CharField(max_length=50, verbose_name="Имя клиента"),
        ),
        migrations.AlterField(
            model_name="lead",
            name="last_name",
            field=models.CharField(max_length=50, verbose_name="Фамилия клиента"),
        ),
        migrations.AlterField(
            model_name="lead",
            name="phone",
            field=models.CharField(
                max_length=12,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Некорректный номер", regex="^\\+7\\d{10}"
                    )
                ],
                verbose_name="Телефон",
            ),
        ),
    ]
