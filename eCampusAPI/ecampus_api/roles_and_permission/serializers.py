from django.contrib.auth.models import Group as Role, Permission
from rest_framework import serializers
from django.conf import settings
from api_authentication.views import is_superuser_id
from employee.models import Department

class DepartmentSerizlizer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions', 'department']
        # extra_kwargs = {'permissions': {'required': False}}

class ListPermissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = ['id', 'name']
