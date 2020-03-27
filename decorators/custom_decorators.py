from django.http import JsonResponse

# custom app model
from auth_api.models import Token


# Class-based Decorator
class CheckToken():
    def __init__(self, func):
        self.__func = func

    def __call__(self, request):
        if request.headers['Token']:
            token = request.headers['Token']
            matched_token = Token.objects.get(token=token)
            if matched_token:
                print("token: {}".format(matched_token))
                return self.__func(request)
            else:
                return JsonResponse({'message': 'Token Not Matched!'}, status=401)
        else:
            return JsonResponse({'message': 'Token Not Found!'}, status=404)


# # Function-based Decorator
# def check_token(func):
#     def wrapper(request):
#         if request.headers['Token']:
#             print(request.headers['Token'])
#             return func(request)
#         else:
#             print('Token Not Found!')
#
#     return wrapper

