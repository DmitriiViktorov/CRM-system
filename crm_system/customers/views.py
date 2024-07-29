from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from crm_system.mixins import GroupPermissionMixin

from .models import Customer


class BaseCustomerView(GroupPermissionMixin, View):
    edit_groups = ['Managers']
    model = Customer


class CustomerListView(BaseCustomerView, ListView):
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomerCreateView(BaseCustomerView, CreateView):
    template_name = 'customers/customers-create.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class CustomerDetailView(BaseCustomerView, DetailView):
    template_name = 'customers/customers-detail.html'


class CustomerUpdateView(BaseCustomerView, UpdateView):
    template_name = 'customers/customers-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('customers-list')


class CustomerDeleteView(BaseCustomerView, DeleteView):
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers-list')

