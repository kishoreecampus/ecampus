from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from employee import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Employee
from api_authentication import permissions as api_permissions
from .permissions import EmployeeHasPermission
from django.conf import settings

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeeSerializer

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

