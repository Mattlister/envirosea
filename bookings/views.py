from django.shortcuts import render
from .models import Booking

# Create your views here.


def all_bookings(request):
    """ A view to show all products, including sorting and search queries """

    bookings = Booking.objects.all()

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/bookings.html', context)
