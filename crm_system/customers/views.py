from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customers-create.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customers-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('customers-list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers-list')
