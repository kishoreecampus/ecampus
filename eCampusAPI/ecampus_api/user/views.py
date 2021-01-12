from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, UserGroupSerializer, ListPermissionSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import User
from api_authentication import permissions as api_permissions
from .permissions import UserHasPermission, UserHasSpecificPermission
from django.conf import settings

class UserInformation(APIView):

    def get(self, request):
        content = {'user': str(request.user), 'first_name': str(request.user.uid) }
        return Response(content)

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = UserGroupSerializer
    permission_classes = [IsAuthenticated, UserHasPermission]

class ListPermission(APIView, UserHasSpecificPermission):

    def get(self, request):
        if self.has_specific_permission(request, 'auth.view_permission') or request.user.is_superuser:
            queryset = Permission.objects.values('id', 'name').filter(content_type__app_label__in=settings.PERMISSION_APP_NAMES, content_type__model__in=settings.PERMISSION_MODEL_NAMES)
        else:
            queryset = {'details':'You don not have permission to perform this action'}
        return Response(queryset)