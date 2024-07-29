from django.db import models
from django.utils import timezone

from leads.models import Lead
from contracts.models import Contract


class Customer(models.Model):
    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name='customer',
        verbose_name='Потенциальный клиент'
    )
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name='customer',
        verbose_name='Контракт'
    )
    activation_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата активации клиента'
    )

    def __str__(self):
        return f"Customer: {self.lead.full_name}"

    @property
    def full_name(self):
        return self.lead.full_name

    @property
    def email(self):
        return self.lead.email

    @property
    def phone(self):
        return self.lead.phone



