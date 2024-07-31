from django.db import models
from django.db.models import Sum

from products.models import Product
from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead


class Ads(models.Model):
    """
    Модель для рекламных компаний.

    Атрибуты:
        name (str): Название рекламной компании
        promotion_channel (str): Канал продвижения
        budget (float): Бюджет на рекламную компанию
        promoted_product (Product): Услуга, которую рекламируют в этой компании.
    """
    name = models.CharField(
        max_length=255,
        verbose_name='Название рекламной компании'
    )
    promotion_channel = models.CharField(
        max_length=255,
        verbose_name='Канал продвижения'
    )
    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Бюджет на рекламу'
    )
    promoted_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Рекламируемая услуга'
    )

    def __str__(self):
        """Возвращает имя рекламной компании при отображении в шаблоне."""
        return str(self.name)

    @property
    def leads_count(self):
        """
        Свойство рекламной компании, возвращает количество потенциальных клиентов, которые указали
        эту рекламную компанию как источник информации об услуге.
        Возвращает:
            Количество потенциальных клиентов, узнавших об услуге из рекламной компании.
        """
        return self.leads.count()

    @property
    def customers_count(self):
        """
        Свойство рекламной компании, возвращает число активных клиентов, перешедших из потенциальных
        Возвращает:
            Количество активных клиентов.
        """
        return self.leads.filter(customer__isnull=False).count()

    @property
    def profit(self):
        """
        Свойство рекламной компании, возвращает коэффициент эффективности рекламной компании
        Возвращает:
            Отношение прибыли от контрактов активных клиентов к затратам на рекламную компанию
        """
        related_leads = Lead.objects.filter(ads=self)
        related_customers = Customer.objects.filter(lead__in=related_leads)

        related_contracts = Contract.objects.filter(
            product=self.promoted_product,
            customer__in=related_customers
        )
        total_contract_cost = related_contracts.aggregate(Sum('cost'))['cost__sum'] or 0

        if self.budget:
            return round((float(total_contract_cost) / float(self.budget)), 2)
        return 0
