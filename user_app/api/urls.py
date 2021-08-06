

from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import RegistrationAV,LogoutAV
urlpatterns = [

    path('login/',obtain_auth_token),
    path('register/',RegistrationAV.as_view()),
    path('logout/',LogoutAV.as_view()),
]