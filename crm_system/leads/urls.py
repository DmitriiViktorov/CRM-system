from django.urls import path, include

from .views import LeadListView, LeadCreateView, LeadDetailView, LeadUpdateView, LeadDeleteView

urlpatterns = [
    path('', LeadListView.as_view(), name='leads-list'),
    path('new/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='lead-edit'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
]
