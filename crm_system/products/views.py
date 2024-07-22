from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/products-create.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/products-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('product-list')
