from django.db import models
from django.utils import timezone

from leads.models import Lead
from contracts.models import Contract


class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.PROTECT, related_name='customer')
    activation_date = models.DateTimeField(default=timezone.now)
    # notes = models.TextField(blank=True, null=True)

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



