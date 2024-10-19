from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return request.method in SAFE_METHODS or request.user.is_superuser
