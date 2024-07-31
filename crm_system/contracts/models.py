import os
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from django.utils import timezone

from products.models import Product


def contract_directory_path(instance, filename):
    """Функция для формирования пути для хранения документов контракта"""
    return f'contracts/product_{instance.id}/{filename}'


class Contract(models.Model):
    """
    Модель для контракта.

    Атрибуты:
        name (str): Название контракта.
        product (Product): Услуга, которая будет оказана по контракту.
        documents (file): Документы, связанные с этим контрактом.
        start_date (date): Дата начала контракта.
        end_date (date): Дата окончания контракта.
        cost (float): Стоимость контракта.

    """
    name = models.CharField(
        max_length=255,
        verbose_name='Название контракта',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Предоставляемая по контракту услуга'
    )
    documents = models.FileField(
        upload_to=contract_directory_path,
        verbose_name='Файл контракта',
        null=True,
        blank=True
    )
    start_date = models.DateField(
        verbose_name='Дата начала действия контракта',
    )
    end_date = models.DateField(
        verbose_name='Дата окончания действия контракта',
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость контракта'
    )

    def clean(self):
        """
        Проверяет правильность введенных данных при создании.

        Проверяет, чтобы дата начала контракта была не раньше текущей даты
        и чтобы дата окончания контракта была не раньше даты начала контракта.

        Возвращает:
            Очищенные данные формы

        Вызывает:
            forms.ValidationError: если дата начала контракта раньше текущей даты
            или дата окончания контракта раньше даты начала контракта
        """
        if self.start_date and self.start_date < timezone.now().date():
            raise ValidationError(
                {
                    'start_date': 'Дата начала контракта не может быть раньше сегодняшнего дня.'
                }
            )

        if self.start_date and self.end_date and self.end_date <= self.start_date:
            raise ValidationError(
                {
                    'end_date': 'Дата окончания контракта должна быть позже даты его начала.'
                }
            )

    def save(self, *args, **kwargs):
        """
        Метод переопределен для корректного сохранения документов.
        Сохраняет загруженный документ во временную папку, после чего сохраняет
        контракт, получает его pk (идентификатор) и на его основе создает
        директорию для хранения документа, а так же записывает путь к документу
        в атрибуты самого контракта.
        """
        if self.pk is None:
            super().save(*args, **kwargs)

            if self.documents:
                new_path = (f'contracts/product_{self.product.primary_key}'
                            f'/contract_{self.pk}/{self.documents.name.split("/")[-1]}')
                old_path = self.documents.path
                new_full_path = os.path.join(settings.MEDIA_ROOT, new_path)

                os.makedirs(os.path.dirname(new_full_path), exist_ok=True)

                os.rename(old_path, new_full_path)

                self.documents = new_path
                super().save(update_fields=['documents'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        """Возвращает имя контракта при отображении в шаблоне."""
        return str(self.name)
