# Generated by Django 5.0.7 on 2024-07-23 12:09

import contracts.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0004_remove_contract_customer"),
        ("products", "0002_rename_price_product_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="cost",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Стоимость контракта"
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="documents",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=contracts.models.contract_directory_path,
                verbose_name="Файл контракта",
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="end_date",
            field=models.DateField(verbose_name="Дата окончания действия контракта"),
        ),
        migrations.AlterField(
            model_name="contract",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Название контракта"),
        ),
        migrations.AlterField(
            model_name="contract",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
                verbose_name="Предоставляемая по контракту услуга",
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="start_date",
            field=models.DateField(verbose_name="Дата начала действия контракта"),
        ),
    ]
