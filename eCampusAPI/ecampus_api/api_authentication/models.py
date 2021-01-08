from django.db import models
from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
from rest_framework_api_key.models import AbstractAPIKey
from rest_framework_api_key.models import BaseAPIKeyManager
from rest_framework_api_key.crypto import KeyGenerator

# @receiver(signals.post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=False, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class OrganizationAPIKeyManager(BaseAPIKeyManager):
    key_generator = KeyGenerator(prefix_length=8, secret_key_length=64)

    def get_usable_keys(self):
        return super().get_usable_keys().filter(organization__active=True)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

class OrganizationAPIKey(AbstractAPIKey):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='api_key')
    objects = OrganizationAPIKeyManager()
