from django.contrib import admin
from django.urls import path , include
from .views import create_api

urlpatterns = [
    path('create/' , create_api , name='Test')
]
