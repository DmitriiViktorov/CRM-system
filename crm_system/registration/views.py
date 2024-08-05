from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm


def login_view(request):
    """
    Обрабатывает запросы на вход пользователя в систему.

    При GET-запросе отображает форму входа.
    При POST-запросе выполняет аутентификацию пользователя.

    Аргументы:
        request (HttpRequest): Объект запроса Django

    Возвращает:
        При успешной аутентификации - редирект на домашнюю страницу.
        В остальных случаях - отрисовывает страницу входа с формой.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                # messages.success(request, 'You are now logged in')
                return redirect('home')
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    """
    Обрабатывает запрос на выход пользователя из системы.

    Аргументы:
        request (HttpRequest): Объект запроса Django

    Возвращает:
        Редирект на домашнюю страницу.
    """
    logout(request)
    # messages.success(request, 'You are now logged out')
    return redirect('home')
