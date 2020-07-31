from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.oceans, name='oceans'),
    path('', views.why, name='why'),
]
