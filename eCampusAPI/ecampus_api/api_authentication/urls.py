from django.urls import path, include
from api_authentication.views import APIObtainAcessToken
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('obtain-access-token/', APIObtainAcessToken.as_view(), name='token_obtain_pair'),
]