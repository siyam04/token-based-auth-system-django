from django.urls import path

from .views import login


app_name = 'auth_api'


urlpatterns = [

    path('login/', login, name='login'),

]

