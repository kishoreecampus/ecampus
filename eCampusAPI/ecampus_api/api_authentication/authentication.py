from rest_framework.authentication import TokenAuthentication


class APITokenAuthentication(TokenAuthentication):
    keyword = 'ecampus'


