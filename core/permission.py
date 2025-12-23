from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'userprofile') and \
               request.user.userprofile.role == 'ADMIN'


class IsAnalystReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return hasattr(request.user, 'userprofile') and \
               request.user.userprofile.role == 'ADMIN'
