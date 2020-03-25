from pprint import pprint
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods

# auth user model
from django.contrib.auth.models import User

# custom app model
from .models import Token


# signup api
@csrf_exempt
@require_http_methods(["POST"])
def sign_up(request):
    # getting api data
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    # if data available
    if username and  email and password and first_name and last_name:
        # user creation
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # modifying data to json format
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

        # return api response
        return JsonResponse(user_data, status=201)

    # if data not available
    else:
        return JsonResponse({'message': 'Signup Failed!'}, status=404)


# login api
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    # getting api data
    username = request.POST.get('username')
    password = request.POST.get('password')

    # if data available
    if username and password:

        # checking
        authenticated = authenticate(username=username, password=password)

        # if authenticated user
        if authenticated:
            # generating token
            token = generate_token()

            # creating object
            Token.objects.create(user=authenticated, token=token)

            # if succeed
            return JsonResponse({'token': token}, status=200)

        # if not succeed
        else:
            return JsonResponse({'message': 'Login Failed!'}, status=401)

    # if data not available
    else:
        return JsonResponse({'message': 'Not Found!'}, status=404)


# logout api
def logout(request):
    # getting token
    token = request.headers['Token']

    # if token available
    if token:
        # matching api token with db token
        matched_token = Token.objects.get(token=token)
        # deleting db token
        matched_token.delete()

        # if succeed
        return JsonResponse({'message': 'Logout Successfully!'}, status=200)

    # if not succeed
    else:
        return JsonResponse({'message': 'Not Found!'}, status=404)


# custom token generating
def generate_token():
    import time

    return str(int(time.time()))



