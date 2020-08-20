from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_person, name='view_person'),
    path('add/<item_id>/', views.add_person, name='add_person'),
]
