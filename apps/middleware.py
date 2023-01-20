from django.conf import settings
from django import http


class BlockedIpMiddleware:
    def __init__(self, get_response):
        # One-time configuration and initialization, when the webserver starts.
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (and later
        # middleware) are called.
        print(request.META['REMOTE_ADDR'])
        if request.META['REMOTE_ADDR'] in settings.BLOCKED_IPS:
            # if request.META['HTTP_X_REAL_IP'] in settings.BLOCKED_IPS:
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')

        return self.get_response(request)
