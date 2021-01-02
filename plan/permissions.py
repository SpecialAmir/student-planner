from rest_framework import permissions

class IsOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user is obj.user or request.user.is_staff:
            return True
        else:
            return False
