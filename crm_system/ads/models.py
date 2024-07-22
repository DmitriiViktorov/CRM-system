from django.db import models
from products.models import Product


class Ads(models.Model):
    name = models.CharField(max_length=255)
    promotion_channel = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    promoted_product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

