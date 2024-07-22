
import os
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from products.models import Product


def contract_directory_path(instance, filename):
    return 'contracts/product_{0}/{1}'.format(instance.id, filename)


class Contract(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    documents = models.FileField(upload_to=contract_directory_path, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.start_date and self.start_date < timezone.now().date():
            raise ValidationError({'start_date': 'Дата начала контракта не может быть раньше сегодняшнего дня.'})

        if self.start_date and self.end_date and self.end_date <= self.start_date:
            raise ValidationError({'end_date': 'Дата окончания контракта должна быть позже даты его начала.'})

    def save(self, *args, **kwargs):
        if self.id is None:
            super().save(*args, **kwargs)

            if self.documents:
                new_path = f'contracts/product_{self.product.id}/contract_{self.id}/{self.documents.name.split("/")[-1]}'
                old_path = self.documents.path
                new_full_path = os.path.join(settings.MEDIA_ROOT, new_path)

                os.makedirs(os.path.dirname(new_full_path), exist_ok=True)

                os.rename(old_path, new_full_path)

                self.documents = new_path
                super().save(update_fields=['documents'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
