from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied


class GroupPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Миксин для обеспечения ограничения доступа к приложениям в зависимости от роли пользователя.

    Позволяет раздельно предоставлять разрешение на полный доступ
    к приложениям и разрешение на просмотр записей.
    При добавлении миксина к View классу необходимо
    указать нужные группы в соответствующих атрибутах
    view_group и/или edit_group, для которых предоставляется разрешения.
    """
    view_groups = []
    edit_groups = []

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False

        user_groups = set(self.request.user.groups.values_list('name', flat=True))

        if set(self.edit_groups) & user_groups or self.request.user.is_superuser:
            return True

        if set(self.view_groups) & user_groups or self.request.user.is_superuser:
            if self.request.method not in ['GET', 'HEAD']:
                return True
            raise PermissionDenied('You are not allowed to access this page.')
        return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return render(self.request, '403.html', status=403)
        return redirect(self.get_login_url())
