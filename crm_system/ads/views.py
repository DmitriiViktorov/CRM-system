from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from crm_system.mixins import GroupPermissionMixin

from .models import Ads


class BaseAdsView(GroupPermissionMixin, View):
    edit_groups = ['Marketologists']
    model = Ads


class AdsListView(BaseAdsView, ListView):
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'


class AdsCreateView(BaseAdsView, CreateView):
    template_name = 'ads/ads-create.html'
    fields = '__all__'
    success_url = reverse_lazy('ads-list')


class AdsDetailView(BaseAdsView, DetailView):
    template_name = 'ads/ads-detail.html'


class AdsUpdateView(BaseAdsView, UpdateView):
    template_name = 'ads/ads-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('ads-list')


class AdsDeleteView(BaseAdsView, DeleteView):
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads-list')


class AdsStatisticView(ListView):
    model = Ads
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'
