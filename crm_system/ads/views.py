from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Ads


class AdsListView(ListView):
    model = Ads
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'


class AdsCreateView(CreateView):
    model = Ads
    template_name = 'ads/ads-create.html'
    fields = '__all__'
    success_url = reverse_lazy('ads-list')


class AdsDetailView(DetailView):
    model = Ads
    template_name = 'ads/ads-detail.html'


class AdsUpdateView(UpdateView):
    model = Ads
    template_name = 'ads/ads-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('ads-list')


class AdsDeleteView(DeleteView):
    model = Ads
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads-list')
