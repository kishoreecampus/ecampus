from django.urls import path, include
from .views import DepartmentViewSet, RoleViewSet, ListPermission
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('department/list/', DepartmentViewSet.as_view({'get':'list'}), name='list_department'),
    path('department/create/', DepartmentViewSet.as_view({'post':'create'}), name='create_department'),
    path('department/update/<pk>/', DepartmentViewSet.as_view({'put':'update'}), name='update_department'),
    path('department/delete/<pk>/', DepartmentViewSet.as_view({'delete':'destroy'}), name='delete_department'),
    path('permissions/', ListPermission.as_view(), name='list_permission'),
    path('role/list/', RoleViewSet.as_view({'get':'list'}), name='list_role'),
    path('role/create/', RoleViewSet.as_view({'post':'create'}), name='create_role'),
    path('role/update/<pk>/', RoleViewSet.as_view({'put':'update'}), name='update_role'),
    path('role/delete/<pk>/', RoleViewSet.as_view({'delete':'destroy'}), name='delete_role'),
]