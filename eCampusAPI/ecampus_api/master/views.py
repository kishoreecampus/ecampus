from django.shortcuts import render
from .models import Profile,ClassGroup,ClassName,Section,Caste,Category
from .serializers import Profile,ProfileCreateSerializer,ProfileDetailSerializer,ProfileUpdateSerializer,ClassGroupSerializer,ClassGroupCreateSerializer,ClassGroupDetailSerializer,ClassGroupUpdateSerializer
from rest_framework import generics
from rest_framework import viewsets
from master import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api_authentication import permissions as api_permissions
from employee.permissions import EmployeeHasPermission, EmployeeHasSpecificPermission


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.ProfileCreateSerializer
        if self.action == 'update':
            return serializers.ProfileUpdateSerializer
        if self.action == 'retrieve':
            return serializers.ProfileDetailSerializer
        if self.action == 'list':
            return serializers.ProfileDetailSerializer
        return super(ProfileViewSet, self).get_serializer_class() 

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user  = self.request.user.id
        else:
            user = 0
        serializer.save(created_by=user)

class ClassGroupViewset(viewsets.ModelViewSet):
    queryset = ClassGroup.objects.all()
    serializer_class = serializers.ClassGroupSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.ClassGroupCreateSerializer
        if self.action == 'update':
            return serializers.ClassGroupUpdateSerializer
        if self.action == 'retrieve':
            return serializers.ClassGroupDetailSerializer
        if self.action == 'list':
            return serializers.ClassGroupDetailSerializer
        return super(ClassGroupViewset, self).get_serializer_class()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = self.request.user.id
        else:
            user = 0
        serializer.save(created_by=user)

class ClassNameViewset(viewsets.ModelViewSet):
    queryset = ClassName.objects.all()
    serializer_class = serializers.ClassNameSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.ClassNameCreateSerializer
        if self.action == 'update':
            return serializers.ClassNameUpdateSerializer
        if self.action == 'retrieve':
            return serializers.ClassNameDetailSerializer
        if self.action == 'list':
            return serializers.ClassNameDetailSerializer
        return super(ClassNameViewset, self).get_serializer_class()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = self.request.user.id
        else:
            user = 0
        serializer.save(created_by=user)

class SectionViewset(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = serializers.SectionSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.SectionCreateSerializer
        if self.action == 'update':
            return serializers.SectionUpdateSerializer
        if self.action == 'retrieve':
            return serializers.SectionDetailSerializer
        if self.action == 'list':
            return serializers.SectionDetailSerializer
        return super(SectionViewset, self).get_serializer_class()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = self.request.user.id
        else:
            user = 0
        serializer.save(created_by=user)

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CategoryCreateSerializer
        if self.action == 'update':
            return serializers.CategoryUpdateSerializer
        if self.action == 'retrieve':
            return serializers.CategoryDetailSerializer
        if self.action == 'list':
            return serializers.CategoryDetailSerializer
        return super(SectionViewset, self).get_serializer_class()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = self.request.user.id
        else:
            user = 0
        serializer.save(created_by=user)

class CasteViewset(viewsets.ModelViewSet):
    queryset = Caste.objects.all()
    serializer_class = serializers.CasteSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CasteCreateSerializer
        if self.action == 'update':
            return serializers.CasteUpdateSerializer
        if self.action == 'retrieve':
            return serializers.CasteDetailSerializer
        if self.action == 'list':
            return serializers.CasteDetailSerializer
        return super(SectionViewset, self).get_serializer_class()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = self.request.user.id
        else:
            user = 0
        serializer.save(created_by=user)
