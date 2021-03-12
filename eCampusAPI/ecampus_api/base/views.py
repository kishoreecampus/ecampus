import urllib.request
import urllib.parse
from django.conf import settings
from rest_framework import response, status
from django.shortcuts import get_list_or_404, get_object_or_404

def send_sms(number, message):
    message = settings.SMS_PREFIX + message
    data = urllib.parse.urlencode({'apikey': settings.SMS_API_KEY, 'numbers': number, 'message': message, 'sender': settings.SMS_SENDER_ID})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    smsRes =  urllib.request.urlopen(request, data)
    response = smsRes.read()
    return (response)

class DestroyWithPayloadMixin(object):

     def destroy(self, *args, **kwargs):
         serializer = self.get_serializer(self.get_object())
         super().destroy(*args, **kwargs)
         return response.Response(serializer.data, status=status.HTTP_200_OK)

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.

    Source: https://www.django-rest-framework.org/api-guide/generic-views/#creating-custom-mixins
    Modified to not error out for not providing all fields in the url.
    """

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field):  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj