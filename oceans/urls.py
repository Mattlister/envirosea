from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('oceans', views.oceans, name='oceans'),
]
