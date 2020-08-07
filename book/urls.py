from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_book, name='view_book'),
]
