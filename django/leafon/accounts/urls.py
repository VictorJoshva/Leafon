
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.accounts),
    path('login',views.login),
    path('signup',views.signup),
    path('plant',views.plant),
]
