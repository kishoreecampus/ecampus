from django.urls import path, include
from .views import EmployeeRoleViewSet, ListPermission, EmployeeViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('permissions', ListPermission.as_view(), name='list_permission'),
    path('list', EmployeeViewSet.as_view({'get':'list'}), name='list_emplyee'),
    path('detail/<pk>', EmployeeViewSet.as_view({'get':'retrieve'}), name='profile'),
    path('create', EmployeeViewSet.as_view({'post':'create'}), name='create_employee'),
    path('update/<pk>', EmployeeViewSet.as_view({'put':'update'}), name='update_employee'),
    path('partial-update/<pk>', EmployeeViewSet.as_view({'patch':'partial_update'}), name='partial_update_employee'),
    path('delete/<pk>', EmployeeViewSet.as_view({'delete':'destroy'}), name='delete_employee'),
    path('roles', EmployeeRoleViewSet.as_view({'get':'list'}), name='list_role'),
    path('role/create', EmployeeRoleViewSet.as_view({'post':'create'}), name='create_role'),
    path('role/update/<pk>', EmployeeRoleViewSet.as_view({'put':'update'}), name='update_role'),
    path('role/delete/<pk>', EmployeeRoleViewSet.as_view({'delete':'destroy'}), name='delete_role'),
]