from django.urls import path
from . import views

urlpatterns = [
    path('bookings', views.all_bookings, name='bookings'),
    path('<int:booking_id>', views.booking_detail, name='booking_detail'),
]
