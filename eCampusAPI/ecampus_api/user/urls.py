from django.urls import path, include
from .views import UserRoleViewSet, ListPermission
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('permissions/', ListPermission.as_view(), name='list_permission'),
    path('roles/', UserRoleViewSet.as_view({'get':'list'}), name='list_role'),
    path('role/create', UserRoleViewSet.as_view({'post':'create'}), name='create_role'),
    path('role/update/<pk>', UserRoleViewSet.as_view({'put':'update'}), name='update_role'),
    path('role/delete/<pk>', UserRoleViewSet.as_view({'delete':'destroy'}), name='delete_role'),
]