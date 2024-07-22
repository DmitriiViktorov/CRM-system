from django import forms
from django.utils import timezone

from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and start_date < timezone.now().date():
            raise forms.ValidationError("Дата начала контракта не может быть раньше сегодняшнего дня.")

        if start_date and end_date and end_date <= start_date:
            raise forms.ValidationError("Дата окончания контракта должна быть позже даты его начала.")

        return cleaned_data
