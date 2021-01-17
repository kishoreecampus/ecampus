from django.contrib.auth.models import Group
from rest_framework import permissions 
import copy

def get_user_group(employee):

    try:
        return Group.objects.get(id=employee.id)
    except Group.DoesNotExist:
        return None

class EmployeeHasPermission(permissions.DjangoModelPermissions):
    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

class EmployeeHasSpecificPermission(permissions.BasePermission):

    def has_specific_permission(self, request, permission_name):
        if permission_name in request.user.get_all_permissions():
            return True
        return False

