from django.contrib import admin
from django.urls import path
from app.views import hello_world, login, register, welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('register/', register),
    path('welcome/', welcome)
]
