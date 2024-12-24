from rest_framework import permissions


class IsGeneralPublic(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 1
        return False
