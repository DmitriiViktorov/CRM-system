from django.db import models
from django.core.validators import RegexValidator


class Lead(models.Model):
    """
    Модель для потенциального клиента.

    Атрибуты:
        first_name (str): Имя клиента.
        last_name (str): Фамилия клиента.
        email (str): Электронная почта клиента.
        phone (str): Телефонный номер клиента.
        ads (str): Рекламная акция, из которой он узнал об услуге.
    """
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя клиента'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия клиента'
    )
    email = models.EmailField(
        verbose_name='Электронная почта'
    )
    phone = models.CharField(
        max_length=12,
        verbose_name='Телефон',
        validators=[RegexValidator(
            regex=r'^\+7\d{10}',
            message='Некорректный номер'
        )]
    )
    ads = models.ForeignKey(
        'ads.Ads',
        on_delete=models.CASCADE,
        verbose_name='Рекламная компания, из которой узнал об услуге',
        related_name='leads',
    )

    def __str__(self):
        """Возвращает полное имя клиента при отображении в шаблоне"""
        return self.full_name

    @property
    def full_name(self):
        """Свойство клиента, возвращает полное имя клиента из его имени и фамилии"""
        return f'{self.first_name} {self.last_name}'
