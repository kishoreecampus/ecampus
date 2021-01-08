from django.urls import path, include
from api_authentication.views import ObtainAcessToken, RefreshAccessToken
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('obtain-access-token/', ObtainAcessToken.as_view(), name='token_obtain_pair'),
    path('refresh/access-token/', RefreshAccessToken.as_view(), name='token_refresh'),
]