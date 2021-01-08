from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import datetime
from django.conf import settings

class APIObtainAcessTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(APIObtainAcessTokenSerializer, cls).get_token(user)
        token['username'] = user.username
        return token
    
    def validate(self, attr):
        data = super().validate(attr)
        refresh = self.get_token(self.user)
        data['created_on'] = datetime.datetime.now()
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        data['uid'] = self.user.id
        
        del data['refresh']
        
        return data
