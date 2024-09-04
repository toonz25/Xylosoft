from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admins/', views.admins, name='hello_admins'),
]