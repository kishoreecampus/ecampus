from django.conf import settings
from rest_framework import renderers

class APIJSONRenderer(renderers.JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {}
        if renderer_context is not None:
            status_code = renderer_context['response'].status_code
            response['code'] = status_code
            if status_code in settings.SUCCESS_CODES:
                response['status'] = True
                response['message'] = 'OK'
                response['data'] = [data]
            else:
                response['status'] = False
                response['message'] = [data]
                # response['message'] = [data[message_name][0] if isinstance(data[message_name], list) else data[message_name] for message_name in data]
        return super(APIJSONRenderer, self).render(response, accepted_media_type, renderer_context)
