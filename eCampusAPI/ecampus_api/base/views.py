import urllib.request
import urllib.parse
from django.conf import settings

def send_sms(number, message):
    message = settings.SMS_PREFIX + message
    data = urllib.parse.urlencode({'apikey': settings.SMS_API_KEY, 'numbers': number, 'message': message, 'sender': settings.SMS_SENDER_ID})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    smsRes =  urllib.request.urlopen(request, data)
    response = smsRes.read()
    return (response)