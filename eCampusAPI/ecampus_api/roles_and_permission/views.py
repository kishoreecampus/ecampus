from django.shortcuts import render
from django.contrib.auth.models import Group as Role, Permission
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from . import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api_authentication import permissions as api_permissions
from employee.permissions import EmployeeHasPermission, EmployeeHasSpecificPermission
from django.conf import settings
from employee.models import Department

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerizlizer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer

class ListPermission(APIView, EmployeeHasSpecificPermission):
    permission_classes = [IsAuthenticated, api_permissions.HasOrganizationAPIKey]

    def get(self, request):
        if self.has_specific_permission(request, 'auth.view_permission') or request.user.is_superuser:
            queryset = Permission.objects.values('id', 'name').filter(content_type__app_label__in=settings.PERMISSION_APP_NAMES, content_type__model__in=settings.PERMISSION_MODEL_NAMES)

        else:
            queryset = {'details':'You don not have permission to perform this action'}
        return Response(queryset)
