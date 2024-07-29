from django.db import models
from products.models import Product
from django.db.models import Sum
from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead


class Ads(models.Model):
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
        return self.name

    @property
    def leads_count(self):
        return self.lead_set.count()

    @property
    def customers_count(self):
        return self.lead_set.filter(customer__isnull=False).count()

    @property
    def profit(self):
        related_leads = Lead.objects.filter(ads=self)
        related_customers = Customer.objects.filter(lead__in=related_leads)

        related_contracts = Contract.objects.filter(
            product=self.promoted_product,
            customer__in=related_customers
        )
        total_contract_cost = related_contracts.aggregate(Sum('cost'))['cost__sum'] or 0

        if self.budget:
            return round(float(total_contract_cost) / float(self.budget), 2)
        return 0

