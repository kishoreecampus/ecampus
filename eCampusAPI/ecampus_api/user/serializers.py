from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']
        # extra_kwargs = {'permissions': {'required': False}}

class ListPermissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = ['id', 'name']
