from django.urls import path, include
from .views import DashboardModules

urlpatterns = [
    path('modules/', DashboardModules.as_view(), name='modules'),
]