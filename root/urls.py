"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# DRF authtoken
from rest_framework.authtoken.views import obtain_auth_token

# jwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    # django admin
    path('admin/', admin.site.urls),

    # DRF urls
    path('api-auth/', include('rest_framework.urls')),

    # DRF authtoken
    path('api-token-auth/', obtain_auth_token),

    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # custom app-1 (token-based authentication api)
    path('api/', include('auth_api.urls')),

    # custom app-2 (practice api)
    path('api-drf/', include('practice_api.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


