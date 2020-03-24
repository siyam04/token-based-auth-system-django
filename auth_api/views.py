import json
from pprint import pprint

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Token


# login api
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        username = body_data['username']
        password = body_data['password']

        if username and password:
            authenticated = authenticate(username=username, password=password)

            if authenticated:
                token = generate_token()
                Token.objects.create(user=authenticated, token=token)

                token_dic = {'token': token}

                return JsonResponse(str(token_dic), safe=False)
        else:
            message = 'Not Found!'
            return JsonResponse(message, safe=False)


# custom token generating
def generate_token():
    import base64
    import time

    token = str(time.time())
    token_bytes = token.encode('ascii')
    token_encoding = base64.b64encode(token_bytes)

    return token_encoding



