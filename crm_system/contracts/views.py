import os
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Contract
from .forms import ContractForm
from django.conf import settings
from django.core.files.storage import default_storage


class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'


class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contracts/contracts-create.html'
    form_class = ContractForm
    success_url = reverse_lazy('contracts-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'


class ContractUpdateView(UpdateView):
    model = Contract
    template_name = 'contracts/contracts-edit.html'
    form_class = ContractForm
    success_url = reverse_lazy('contracts-list')

    def form_valid(self, form):
        old_document = None
        if self.object.documents:
            old_document = self.object.documents.path

        new_file = form.cleaned_data.get('documents')
        print('tut noviy fail')
        print(form.cleaned_data)
        response = super().form_valid(form)

        if 'documents' in form.changed_data and new_file:
            if old_document and os.path.exists(old_document):
                os.remove(old_document)

            new_filename = new_file.name
            new_path = f'contracts/product_{self.object.product.id}/contract_{self.object.id}/{new_filename}'
            new_full_path = os.path.join(settings.MEDIA_ROOT, new_path)

            os.makedirs(os.path.dirname(new_full_path), exist_ok=True)

            with default_storage.open(new_path, 'wb+') as destination:
                for chunk in new_file.chunks():
                    destination.write(chunk)

            self.object.documents.name = new_path
            self.object.save(update_fields=['documents'])

        return response


class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts-list')
