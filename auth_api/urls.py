from django.urls import path

# custom app
from .views import sign_up, login, logout


urlpatterns = [

    # sign-up api
    path('sign-up/', sign_up),

    # login api
    path('login/', login),

    # logout api
    path('logout/', logout),

]



