from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from api_authentication.permissions import HasOrganizationAPIKey
from rest_framework_simplejwt import views as jwt_views
from .serializers import ObtainAcessTokenSerializer, RefreshAccessTokenSerializer
from rest_framework.permissions import IsAuthenticated

class ObtainAcessToken(jwt_views.TokenObtainPairView):
    permission_classes = [HasOrganizationAPIKey]
    serializer_class = ObtainAcessTokenSerializer

class RefreshAccessToken(jwt_views.TokenRefreshView):
    permission_classes = [HasOrganizationAPIKey]
    serializer_class = RefreshAccessTokenSerializer

class AuthenticationLogoutView(APIView):
    permissionclasses = [IsAuthenticated, HasOrganizationAPIKey]