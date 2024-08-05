import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.urls import reverse_lazy

from crm_system.mixins import GroupPermissionMixin
from .models import Contract
from .forms import ContractForm


class BaseContractView(GroupPermissionMixin, View):
    """
    Базовое представление для контрактов.

    Обеспечивает общую функциональность для всех представлений,
    связанных с моделью Contract.
    Ограничивает доступ к контрактам определенной группе пользователей.

    Атрибуты:
        edit_groups (list): Список групп, имеющих право редактирования.
        model (Model): Модель, с которой работает представление.
    """
    edit_groups = ['Managers']
    model = Contract


class ContractListView(BaseContractView, ListView):
    """
    Представления для отображения всего списка контрактов.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения списка
        context_object_name (str): Имя переменной контекста для списка объектов.
    """
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'


class ContractCreateView(BaseContractView, CreateView):
    """
    Представления для создание нового контракта.

    Атрибуты:
        template_name (str): Путь к шаблону формы создания.
        form_class (Form): Модель формы, используемая для создания.
        success_url (str): URL для перенаправления после успешного создания.
    """
    template_name = 'contracts/contracts-create.html'
    form_class = ContractForm
    success_url = reverse_lazy('contracts-list')


class ContractDetailView(BaseContractView, DetailView):
    """
    Представления для отображения деталей контракта.

    Атрибуты:
        template_name (str): Путь к шаблону для отображения контракта.
    """
    template_name = 'contracts/contracts-detail.html'


class ContractUpdateView(BaseContractView, UpdateView):
    """
    Представления для редактирования имеющегося контракта.

    Атрибуты:
        template_name (str): Путь к шаблону формы редактирования.
        form_class (Form): Модель формы, используемая для редактирования.
        success_url (str): URL для перенаправления после успешного редактирования.
    """
    template_name = 'contracts/contracts-edit.html'
    form_class = ContractForm
    success_url = reverse_lazy('contracts-list')

    def form_valid(self, form):
        """
        Валидация данных в форме после редактирования.

        Проверяет наличие изменений в поле 'documents' и обновляет
        файл, если он изменился. Удаляет старый файл, если он существует.
        Создает директорию для нового файла, если она не существует.

        Атрибуты:
            form (Form): Проверенная форма контракта.

        Возвращает:
            HttpResponse: Перенаправление на URL успеха после успешного редактирования.
        """
        old_document = None
        if self.object.documents:
            old_document = self.object.documents.path

        new_file = form.cleaned_data.get('documents')
        response = super().form_valid(form)

        if 'documents' in form.changed_data and new_file:
            if old_document and os.path.exists(old_document):
                os.remove(old_document)

            new_filename = new_file.name
            new_path = (f'contracts/product_{self.object.product.id}'
                        f'/contract_{self.object.id}/{new_filename}')
            new_full_path = os.path.join(settings.MEDIA_ROOT, new_path)

            os.makedirs(os.path.dirname(new_full_path), exist_ok=True)

            with default_storage.open(new_path, 'wb+') as destination:
                for chunk in new_file.chunks():
                    destination.write(chunk)

            self.object.documents.name = new_path
            self.object.save(update_fields=['documents'])

        return response


class ContractDeleteView(BaseContractView, DeleteView):
    """
    Представления для удаления имеющегося контракта.

    Атрибуты:
        template_name (str): Путь к шаблону подтверждения удаления.
        success_url (str): URL для перенаправления после успешного удаления.
    """
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts-list')
