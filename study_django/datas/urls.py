# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('login', views.login, name='login'),
]
