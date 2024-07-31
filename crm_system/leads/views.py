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
from .models import Lead


class BaseLeadView(GroupPermissionMixin, View):
    """
    Базовое представление для потенциальных пользователей..

    Обеспечивает общую функциональность для всех представлений,
    связанных с моделью Lead.
    Ограничивает доступ к потенциальным клиентам определенной группе пользователей.

    Атрибуты:
        edit_groups (list): Список групп, имеющих право редактирования.
        view_group (list): Список групп, имеющих право просмотра.
        model (Model): Модель, с которой работает представление.
    """
    edit_groups = ['Operators']
    view_groups = ['Managers']
    model = Lead


class LeadListView(BaseLeadView, ListView):
    """
    Представления для отображения всего списка потенциальных клиентов.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения списка
        context_object_name (str): Имя переменной контекста для списка объектов.
    """
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'


class LeadCreateView(BaseLeadView, CreateView):
    """
    Представления для создания нового потенциального клиента.

    Атрибуты:
        template_name (str): Путь к шаблону формы создания.
        fields (str): Поля модели, используемые в форме.
        success_url (str): URL для перенаправления после успешного создания.
    """
    template_name = 'leads/leads-create.html'
    fields = '__all__'
    success_url = reverse_lazy('leads-list')


class LeadDetailView(BaseLeadView, DetailView):
    """
    Представления для отображения деталей потенциального клиента.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения потенциального клиента.
    """
    template_name = 'leads/leads-detail.html'


class LeadUpdateView(BaseLeadView, UpdateView):
    """
    Представления для редактирования потенциального клиента.

    Атрибуты:
        template_name (str): Путь к шаблону формы редактирования.
        fields (str): Поля модели, используемые в форме.
        success_url (str): URL для перенаправления после успешного редактирования.
    """
    template_name = 'leads/leads-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('leads-list')


class LeadDeleteView(BaseLeadView, DeleteView):
    """
    Представления для удаления потенциального клиента

    Атрибуты:
        template_name (str): Путь к шаблону подтверждения удаления.
        success_url (str): URL для перенаправления после успешного удаления.
    """
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads-list')
