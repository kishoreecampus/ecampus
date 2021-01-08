from django.urls import path, include
from .views import DashboardModules, MasterModules

urlpatterns = [
    path('dashboard/', DashboardModules.as_view(), name='dashboard'),
    path('master/', MasterModules.as_view(), name='master'),
]