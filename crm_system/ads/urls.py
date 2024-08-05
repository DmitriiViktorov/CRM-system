from django.urls import path

from .views import (
    AdsListView,
    AdsDetailView,
    AdsDeleteView,
    AdsCreateView,
    AdsUpdateView,
    AdsStatisticView
)

urlpatterns = [
    path('', AdsListView.as_view(), name='ads-list'),
    path('new/', AdsCreateView.as_view(), name='ads-create'),
    path('<int:pk>/', AdsDetailView.as_view(), name='ads-detail'),
    path('<int:pk>/edit/', AdsUpdateView.as_view(), name='ads-edit'),
    path('<int:pk>/delete/', AdsDeleteView.as_view(), name='ads-delete'),
    path('statistic/', AdsStatisticView.as_view(), name='ads-statistic'),
]
