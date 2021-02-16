import urllib.request
import urllib.parse
from django.conf import settings
from rest_framework import response, status

def send_sms(number, message):
    message = settings.SMS_PREFIX + message
    data = urllib.parse.urlencode({'apikey': settings.SMS_API_KEY, 'numbers': number, 'message': message, 'sender': settings.SMS_SENDER_ID})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    smsRes =  urllib.request.urlopen(request, data)
    response = smsRes.read()
    return (response)

class DestroyWithPayloadMixin(object):

    # Overridding destory method

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
