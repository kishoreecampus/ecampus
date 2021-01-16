from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from user import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import User
from api_authentication import permissions as api_permissions
from .permissions import UserHasPermission, UserHasSpecificPermission
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, api_permissions.HasOrganizationAPIKey, UserHasPermission]

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.UserCreateSerializer
        if self.action == 'update':
            return serializers.UserUpdateSerializer
        if self.action == 'retrieve':
            return serializers.UserDetailSerializer
        if self.action == 'list':
            return serializers.UserDetailSerializer
        if self.action == 'partial_update':
            return serializers.UserPartialUpdateSerializer
        return super(UserViewSet, self).get_serializer_class()

    def get_queryset(self):
        queryset = User.objects.filter(is_superuser=0)
        return queryset

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.UserGroupSerializer
    permission_classes = [IsAuthenticated, UserHasPermission]

class ListPermission(APIView, UserHasSpecificPermission):

    def get(self, request):
        if self.has_specific_permission(request, 'auth.view_permission') or request.user.is_superuser:
            queryset = Permission.objects.values('id', 'name').filter(content_type__app_label__in=settings.PERMISSION_APP_NAMES, content_type__model__in=settings.PERMISSION_MODEL_NAMES)
        else:
            queryset = {'details':'You don not have permission to perform this action'}
        return Response(queryset)

