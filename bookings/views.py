from django.shortcuts import render, get_object_or_404
from .models import Booking

# Create your views here.


def all_bookings(request):
    """ A view to show all products, including sorting and search queries """

    bookings = Booking.objects.all()

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/bookings.html', context)


def booking_detail(request, booking_id):
    """ A view to show individual booking details """

    booking = get_object_or_404(Booking, pk=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'bookings/booking_detail.html', context)
