from rest_framework import permissions

class IsArcheoGeneralAdmin(permissions.BasePermission):
    """
    Custom permission to only allow archeo general admin to access the view.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 1 or request.user.role == 2 or request.user.role == 3
        return False
