from django.shortcuts import render


def custom_permission_denied(request):
    """Хендлер для перенаправления на страницу оповещения об отсутствии разрешений"""
    return render(request, '403.html', status=403)
