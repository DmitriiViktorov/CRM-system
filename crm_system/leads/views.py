from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from crm_system.mixins import GroupPermissionMixin
from .models import Lead


class BaseLeadView(GroupPermissionMixin, View):
    edit_groups = ['Operators']
    view_groups = ['Managers']
    model = Lead


class LeadListView(BaseLeadView, ListView):
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'


class LeadCreateView(BaseLeadView, CreateView):
    template_name = 'leads/leads-create.html'
    fields = '__all__'
    success_url = reverse_lazy('leads-list')


class LeadDetailView(BaseLeadView, DetailView):
    template_name = 'leads/leads-detail.html'


class LeadUpdateView(BaseLeadView, UpdateView):
    template_name = 'leads/leads-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('leads-list')


class LeadDeleteView(BaseLeadView, DeleteView):
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads-list')
