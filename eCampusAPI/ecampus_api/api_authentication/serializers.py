from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
import datetime
from django.conf import settings

class ObtainAcessTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(ObtainAcessTokenSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

    def validate(self, attr):
        data = super(ObtainAcessTokenSerializer, self).validate(attr)
        refresh = self.get_token(self.user)
        data['created_on'] = datetime.datetime.now()
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        data['uid'] = self.user.id
        data['name'] = self.user.first_name
        
        return data

class RefreshAccessTokenSerializer(TokenRefreshSerializer):

    def validate(self, attr):
        data = super(RefreshAccessTokenSerializer, self).validate(attr)
        
        return data