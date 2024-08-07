# Generated by Django 5.0.7 on 2024-07-23 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0005_alter_contract_cost_alter_contract_documents_and_more"),
        ("customers", "0002_remove_customer_notes"),
        ("leads", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="contract",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer",
                to="contracts.contract",
                verbose_name="Контракт",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="customer",
            name="lead",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer",
                to="leads.lead",
                verbose_name="Потенциальный клиент",
            ),
        ),
    ]
