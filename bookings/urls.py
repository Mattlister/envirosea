from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bookings, name='bookings'),
    path('<booking_id>', views.booking_detail, name='booking_detail'),
]
