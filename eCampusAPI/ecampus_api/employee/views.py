from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from employee import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Employee
from api_authentication import permissions as api_permissions
from .permissions import EmployeeHasPermission, EmployeeHasSpecificPermission
from django.conf import settings

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [IsAuthenticated, api_permissions.HasOrganizationAPIKey, EmployeeHasPermission]

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.EmployeeCreateSerializer
        if self.action == 'update':
            return serializers.EmployeeUpdateSerializer
        if self.action == 'retrieve':
            return serializers.EmployeeDetailSerializer
        if self.action == 'list':
            return serializers.EmployeeDetailSerializer
        if self.action == 'partial_update':
            return serializers.EmployeePartialUpdateSerializer
        return super(EmployeeViewSet, self).get_serializer_class()

    def get_queryset(self):
        queryset = Employee.objects.filter(is_superuser=0)
        return queryset

class EmployeeRoleViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.EmployeeGroupSerializer
    permission_classes = [IsAuthenticated, EmployeeHasPermission]

class ListPermission(APIView, EmployeeHasSpecificPermission):

    def get(self, request):
        if self.has_specific_permission(request, 'auth.view_permission') or request.user.is_superuser:
            queryset = Permission.objects.values('id', 'name').filter(content_type__app_label__in=settings.PERMISSION_APP_NAMES, content_type__model__in=settings.PERMISSION_MODEL_NAMES)
        else:
            queryset = {'details':'You don not have permission to perform this action'}
        return Response(queryset)
