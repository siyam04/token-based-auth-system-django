from django.urls import path

from .views import signup, login, logout


app_name = 'auth_api'


urlpatterns = [

    path('signup/', signup),

    path('login/', login),

    path('logout/', logout),

]

