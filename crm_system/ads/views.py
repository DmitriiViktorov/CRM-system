from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from crm_system.mixins import GroupPermissionMixin
from .models import Ads


class BaseAdsView(GroupPermissionMixin, View):
    """
    Базовое представление для рекламных кампаний.

    Обеспечивает общую функциональность для всех представлений,
    связанных с моделью Ads.
    Ограничивает доступ к рекламным компаниям определенной группе пользователей.

    Атрибуты:
        edit_groups (list): Список групп, имеющих право редактирования.
        model (Model): Модель, с которой работает представление.
    """
    edit_groups = ['Marketologists']
    model = Ads


class AdsListView(BaseAdsView, ListView):
    """
    Представления для отображения всего списка доступных рекламных компаний.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения списка
        context_object_name (str): Имя переменной контекста для списка объектов.
    """
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'


class AdsCreateView(BaseAdsView, CreateView):
    """
    Представления для создания новой рекламной компании

    Атрибуты:
        template_name (str): Путь к шаблону формы создания.
        fields (str): Поля модели, используемые в форме.
        success_url (str): URL для перенаправления после успешного создания.
    """
    template_name = 'ads/ads-create.html'
    fields = '__all__'
    success_url = reverse_lazy('ads-list')


class AdsDetailView(BaseAdsView, DetailView):
    """
    Представления для отображения деталей рекламной компании.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения рекламной компании.
    """
    template_name = 'ads/ads-detail.html'


class AdsUpdateView(BaseAdsView, UpdateView):
    """
    Представления для редактирования имеющейся рекламной компании

    Атрибуты:
        template_name (str): Путь к шаблону формы редактирования.
        fields (str): Поля модели, используемые в форме.
        success_url (str): URL для перенаправления после успешного редактирования.
    """
    template_name = 'ads/ads-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('ads-list')


class AdsDeleteView(BaseAdsView, DeleteView):
    """
    Представления для удаления имеющейся рекламной компании

    Атрибуты:
        template_name (str): Путь к шаблону подтверждения удаления.
        success_url (str): URL для перенаправления после успешного удаления.
    """
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads-list')


class AdsStatisticView(ListView):
    """
    Представления для удаления имеющейся рекламной компании

    Атрибуты:
        model (Model): Модель Ads, используемая для получения данных.
        template_name (str): Путь к шаблону статистики рекламных компаний.
        context_object_name (str): Имя переменной контекста для списка объектов.

    """
    model = Ads
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'
