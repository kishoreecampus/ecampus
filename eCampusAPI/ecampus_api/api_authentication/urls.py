from django.urls import path, include
from api_authentication.views import ObtainAcessToken, RefreshAccessToken, AuthenticationLogoutView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('obtain-access-token/', ObtainAcessToken.as_view(), name='login'),
    path('refresh/access-token/', RefreshAccessToken.as_view(), name='token_refresh'),
    path('account/logout', AuthenticationLogoutView.as_view(), name='logout'),
]