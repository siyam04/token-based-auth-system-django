from pprint import pprint
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_http_methods

from django.contrib.auth.models import User

from .models import Token


# signup api
@csrf_exempt
@require_http_methods(["POST"])
def signup(request):
    import json

    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        username = body_data['username']
        password = body_data['password']
        email = body_data['email']
        first_name = body_data['first_name']
        last_name = body_data['last_name']

        if username and password and email and first_name and last_name:
            token = generate_token()

            User.objects.create(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

            formatted_token = json_formatter(token)

            return JsonResponse(formatted_token, safe=False)

        else:
            return JsonResponse('Signup Failed!', safe=False)


# login api
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    import json

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

                formatted_token = json_formatter(token)
                print(type(formatted_token))

                return JsonResponse(formatted_token, safe=False)

            else:
                return JsonResponse('Login Failed!', safe=False)


# custom token generating
def generate_token():
    import base64
    import time

    token = str(time.time())
    token_bytes = token.encode('ascii')
    token_encoding = base64.b64encode(token_bytes)

    return token_encoding


# json formatter
# ToDo: not returning JSON, returns string
def json_formatter(object):
    import json

    decoding_object = object.decode('utf-8')
    jsonifyed_object = json.dumps(decoding_object)

    return jsonifyed_object

#################################################################################################

# logout api
# @csrf_exempt
# @login_required
# @require_http_methods(["POST"])
# def logout(request):
#     logout(request)
#     return JsonResponse('Logout Successfully!', safe=False)



