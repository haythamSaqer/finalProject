from rest_framework import permissions

from .models import Contract


class ContractApprovePermission(permissions.BasePermission):
    message = "Approve contract permission deny"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
        else:
            return False
