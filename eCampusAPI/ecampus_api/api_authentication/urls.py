from django.urls import path, include
from api_authentication.views import ApiObtainAuthToken

urlpatterns = [
    path('obtain-auth-token', ApiObtainAuthToken.as_view())
]