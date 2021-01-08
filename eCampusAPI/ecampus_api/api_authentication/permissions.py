from rest_framework_api_key.permissions import BaseHasAPIKey
from .models import OrganizationAPIKey
from rest_framework import permissions

class HasOrganizationAPIKey(BaseHasAPIKey):
    model = OrganizationAPIKey

class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser