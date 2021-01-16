from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from .models import User
from django.conf import settings
from api_authentication.views import is_superuser_id

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'groups', 'is_active']

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        return validated_data

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'groups', 'is_active']

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'groups', 'is_active']

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        return validated_data

class UserPartialUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['is_active']

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'groups', 'is_active']

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']
        # extra_kwargs = {'permissions': {'required': False}}

class ListPermissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = ['id', 'name']
