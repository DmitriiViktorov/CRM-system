from django import forms


class LoginForm(forms.Form):
    """Форма для авторизации пользователя."""
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
