from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView,
    View
)
from django.urls import reverse_lazy
from crm_system.mixins import GroupPermissionMixin

from .models import Product


class BaseProductView(GroupPermissionMixin, View):
    """
    Базовое представление для услуги.

    Обеспечивает общую функциональность для всех представлений,
    связанных с моделью Product.
    Ограничивает доступ к услугам определенной группе пользователей.

    Атрибуты:
        edit_groups (list): Список групп, имеющих право редактирования.
        model (Model): Модель, с которой работает представление.
    """
    edit_groups = ['Marketologists']
    model = Product


class ProductListView(BaseProductView, ListView):
    """
    Представления для отображения всего списка доступных услуг.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения списка
        context_object_name (str): Имя переменной контекста для списка объектов.
    """
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ProductCreateView(BaseProductView, CreateView):
    """
    Представления для создания новой услуги

    Атрибуты:
        template_name (str): Путь к шаблону формы создания.
        fields (str): Поля модели, используемые в форме.
        success_url (str): URL для перенаправления после успешного создания.
    """
    template_name = 'products/products-create.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDetailView(BaseProductView, DetailView):
    """
    Представления для отображения деталей услуги.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения услуги.
    """
    template_name = 'products/products-detail.html'


class ProductUpdateView(BaseProductView, UpdateView):
    """
    Представления для редактирования услуги

    Атрибуты:
        template_name (str): Путь к шаблону формы редактирования.
        fields (str): Поля модели, используемые в форме.
        success_url (str): URL для перенаправления после успешного редактирования.
    """
    template_name = 'products/products-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(BaseProductView, DeleteView):
    """
    Представления для удаления услуги

    Атрибуты:
        template_name (str): Путь к шаблону подтверждения удаления.
        success_url (str): URL для перенаправления после успешного удаления.
    """
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('product-list')
