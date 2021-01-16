from django.urls import path, include
from .views import UserRoleViewSet, ListPermission, UserViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('permissions', ListPermission.as_view(), name='list_permission'),
    path('list', UserViewSet.as_view({'get':'list'}), name='list_users'),
    path('detail/<pk>', UserViewSet.as_view({'get':'retrieve'}), name='profile'),
    path('create', UserViewSet.as_view({'post':'create'}), name='create_user'),
    path('update/<pk>', UserViewSet.as_view({'put':'update'}), name='update_user'),
    path('partial-update/<pk>', UserViewSet.as_view({'patch':'partial_update'}), name='partial_update_user'),
    path('delete/<pk>', UserViewSet.as_view({'delete':'destroy'}), name='delete_user'),
    path('roles', UserRoleViewSet.as_view({'get':'list'}), name='list_role'),
    path('role/create', UserRoleViewSet.as_view({'post':'create'}), name='create_role'),
    path('role/update/<pk>', UserRoleViewSet.as_view({'put':'update'}), name='update_role'),
    path('role/delete/<pk>', UserRoleViewSet.as_view({'delete':'destroy'}), name='delete_role'),
]