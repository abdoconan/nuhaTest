from django.http import HttpResponse
import json
from django.conf import settings
import os
import re
from knox.auth import TokenAuthentication


class AuthinticationMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):

        returned_value = self.process_request(request, *args, **kwargs)
        if returned_value != 1:
            return HttpResponse("Unauthorized", status=401)

        response = self.get_response(request, *args, **kwargs)

        return response

    def process_request(self, request, *args, **kwargs):
        UrlsPermssion = os.path.join(settings.BASE_DIR, 'UrlsPermssion.json')
        urls_object = {}
        knox_authontication = TokenAuthentication()
        with open(UrlsPermssion) as jsonFile:
            urls_object = json.load(jsonFile)

        for url_object in urls_object:
            url = url_object['url']
            methods = url_object['methods']
            # if re.match(url, request.path, re.IGNORECASE) and (request.method in methods):
            if url == request.path and (request.method in methods):
                try:
                    user, auth_token = knox_authontication.authenticate(
                        request)
                    return 1
                except Exception as e:
                    return -1

        return 1
