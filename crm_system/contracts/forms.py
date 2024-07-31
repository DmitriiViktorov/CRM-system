from django import forms
from django.utils import timezone

from .models import Contract


class ContractForm(forms.ModelForm):
    """
    Форма для создания нового контракта.

    Атрибуты:
        model (Model): Модель, с которой связана форма.
        fields (str): Поля модели, которые будут включены в форму.
        widgets (dict): Настройки виждетов для полей формы.

    """
    class Meta:
        """
        Метаданные для формы ContractForm.

        Атрибуты:
            model (Model): Модель, с которой связана форма.
            fields (str): Поля модели, которые будут включены в форму.
            widgets (dict): Настройки виджетов для полей формы.
        """
        model = Contract
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        """
        Проверяет правильность введенных данных в форме

        Проверяет, чтобы дата начала контракта была не раньше текущей даты
        и чтобы дата окончания контракта была не раньше даты начала контракта.

        Возвращает:
            Очищенные данные формы

        Вызывает:
            forms.ValidationError: если дата начала контракта раньше текущей даты
            или дата окончания контракта раньше даты начала контракта
        """
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and start_date < timezone.now().date():
            raise forms.ValidationError(
                "Дата начала контракта не может быть раньше сегодняшнего дня."
            )

        if start_date and end_date and end_date <= start_date:
            raise forms.ValidationError(
                "Дата окончания контракта должна быть позже даты его начала."
            )

        return cleaned_data
