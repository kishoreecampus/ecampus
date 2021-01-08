from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ModuleSerializer
from .models import Module
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAdminUser
from api_authentication.permissions import HasOrganizationAPIKey, IsSuperUser
from rest_framework import generics

class DashboardModules(generics.ListAPIView):
    # permission_classes = [IsSuperUser]
    serializer_class = ModuleSerializer

    def get_queryset(self):
        queryset = Module.objects
        if self.request.user.is_superuser:
            queryset = queryset
        else:
            modules = self.request.user.modules
            queryset = queryset.filter(id__in=modules.split(","))
        queryset = queryset.filter(is_active=True)
        return queryset


        
