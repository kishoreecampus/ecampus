from django.contrib.auth.models import Group as Role, Permission
from rest_framework import serializers
from .models import Employee
from django.conf import settings
from api_authentication.views import is_superuser_id

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'mobile', 'groups', 'is_active']

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        return validated_data

class EmployeeCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'mobile', 'groups', 'is_active']

    def create(self, validated_data):
        user = super(EmployeeCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class EmployeeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'groups', 'mobile', 'is_active']

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        return validated_data

class EmployeePartialUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['is_active']

class EmployeeDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'username', 'email', 'mobile', 'groups', 'is_active']

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

class EmployeeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions', 'department']
        # extra_kwargs = {'permissions': {'required': False}}

class ListPermissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = ['id', 'name']
