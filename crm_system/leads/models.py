from django.db import models
from django.core.validators import RegexValidator


class Lead(models.Model):
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
        verbose_name='Рекламная компания, из которой узнал об услуге'
    )

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

