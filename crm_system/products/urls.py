from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    ProductDeleteView,
    ProductCreateView,
    ProductUpdateView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('new/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
