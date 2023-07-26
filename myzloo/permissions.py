from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_staff:
            return True
        return False

class IsAuthenticatedOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.user.is_authenticated:
            return True
        return False