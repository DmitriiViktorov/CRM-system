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
from .models import Customer


class BaseCustomerView(GroupPermissionMixin, View):
    """
    Базовое представление для активного клиента.

    Обеспечивает общую функциональность для всех представлений,
    связанных с моделью Customer.
    Ограничивает доступ к активным клиентам определенной группе пользователей.

    Атрибуты:
        edit_groups (list): Список групп, имеющих право редактирования.
        model (Model): Модель, с которой работает представление.
    """
    edit_groups = ['Managers']
    model = Customer


class CustomerListView(BaseCustomerView, ListView):
    """
    Представления для отображения всего списка доступных активных клиентов.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения списка
        context_object_name (str): Имя переменной контекста для списка объектов.
    """
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomerCreateView(BaseCustomerView, CreateView):
    """
    Представления для создания нового активного клиента

    Атрибуты:
        template_name (str): Путь к шаблону формы создания.
        fields (str): Поля модели, используемые в форме.
        success_url (str): URL для перенаправления после успешного создания.
    """
    template_name = 'customers/customers-create.html'
    fields = '__all__'
    success_url = reverse_lazy('customers-list')


class CustomerDetailView(BaseCustomerView, DetailView):
    """
    Представления для отображения деталей активного клиента.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения активного клиента.
    """
    template_name = 'customers/customers-detail.html'


class CustomerUpdateView(BaseCustomerView, UpdateView):
    """
    Представления для редактирования имеющихся активных клиентов

    Атрибуты:
        template_name (str): Путь к шаблону формы редактирования.
        fields (str): Поля модели, используемые в форме.
        success_url (str): URL для перенаправления после успешного редактирования.
    """
    template_name = 'customers/customers-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('customers-list')


class CustomerDeleteView(BaseCustomerView, DeleteView):
    """
    Представления для удаления активного клиента

    Атрибуты:
        template_name (str): Путь к шаблону подтверждения удаления.
        success_url (str): URL для перенаправления после успешного удаления.
    """
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers-list')
