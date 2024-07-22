from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Lead


class LeadListView(ListView):
    model = Lead
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'


class LeadCreateView(CreateView):
    model = Lead
    template_name = 'leads/leads-create.html'
    fields = '__all__'
    success_url = reverse_lazy('leads-list')


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'


class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'leads/leads-edit.html'
    fields = '__all__'
    success_url = reverse_lazy('leads-list')


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads-list')
