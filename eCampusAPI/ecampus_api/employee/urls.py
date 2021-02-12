from django.urls import path, include
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
 
    path('list/', EmployeeViewSet.as_view({'get':'list'}), name='list_emplyee'),
    path('detail/<pk>/', EmployeeViewSet.as_view({'get':'retrieve'}), name='profile'),
    path('create/', EmployeeViewSet.as_view({'post':'create'}), name='create_employee'),
    path('update/<pk>/', EmployeeViewSet.as_view({'put':'update'}), name='update_employee'),
    path('partial-update/<pk>/', EmployeeViewSet.as_view({'patch':'partial_update'}), name='partial_update_employee'),
    path('delete/<pk>/', EmployeeViewSet.as_view({'delete':'destroy'}), name='delete_employee'),
]