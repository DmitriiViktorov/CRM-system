from django.urls import path, include

from .views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='user-login'),
    path('logout/', logout_view, name='user-logout'),
]
