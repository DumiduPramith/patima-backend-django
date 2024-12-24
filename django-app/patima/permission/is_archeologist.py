from rest_framework import permissions


class IsArcheologist(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 2
        return False
