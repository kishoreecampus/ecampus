from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import User
from api_authentication.permissions import HasOrganizationAPIKey

class UserInformation(APIView):

    def get(self, request):
        content = {'user': str(request.user), 'first_name': str(request.user.uid) }
        return Response(content)