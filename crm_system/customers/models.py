from django.db import models
from django.utils import timezone

from leads.models import Lead
from contracts.models import Contract


class Customer(models.Model):
    """
    Модель для активных клиентов.

    Атрибуты:
        lead (Lead): Прошлое состояние клиента - потенциальных клиент
        contract (Contract): Контракт об оказании услуги клиенту
        activation_date (date): Дата перехода из потенциальных клиентов в активные
    """
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
        """Возвращает полное имя клиента при отображении в шаблоне."""
        return f"Customer: {self.full_name}"

    @property
    def full_name(self):
        """Возвращает полное имя клиента"""
        return self.lead.full_name

    @property
    def email(self):
        """Возвращает электронную почту клиента"""
        return self.lead.email

    @property
    def phone(self):
        """Возвращает телефонный номер клиента"""
        return self.lead.phone
