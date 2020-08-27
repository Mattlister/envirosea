from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bookings, name='bookings'),
    path('add/<int:booking_id>', views.add_booking, name='add_booking_to_bag'),
    path('<int:booking_id>', views.booking_detail, name='booking_detail')
]