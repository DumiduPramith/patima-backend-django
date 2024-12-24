from rest_framework import permissions


class IsArcheoLogistOrGeneralPub(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 2 or request.user.role == 1
        return False
