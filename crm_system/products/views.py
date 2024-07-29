from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from crm_system.mixins import GroupPermissionMixin

from .models import Product


class BaseProductView(GroupPermissionMixin, View):
    edit_groups = ['Marketologists']
    model = Product


class ProductListView(BaseProductView, ListView):
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ProductCreateView(BaseProductView, CreateView):
    template_name = 'products/products-create.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDetailView(BaseProductView, DetailView):
    template_name = 'products/products-detail.html'


class ProductUpdateView(BaseProductView, UpdateView):
    template_name = 'products/products-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(BaseProductView, DeleteView):
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('product-list')

