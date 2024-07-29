from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied


class GroupPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    view_groups = []
    edit_groups = []

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False

        user_groups = set(self.request.user.groups.values_list('name', flat=True))

        if set(self.edit_groups) & user_groups:
            return True

        if set(self.view_groups) & user_groups:
            if self.request.method in ['GET', 'HEAD']:
                return True
            else:
                raise PermissionDenied('You are not allowed to access this page.')

        return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return render(self.request, '403.html', status=403)
        return redirect(self.get_login_url())

