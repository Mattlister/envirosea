from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Booking

# Create your views here.


def all_bookings(request):
    """ A view to show all bookings, including sorting and search queries """

    bookings = Booking.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('bookings'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            bookings = bookings.filter(queries)

    context = {
        'bookings': bookings,
        'search_term': query,

    }

    return render(request, 'bookings/bookings.html', context)


def booking_detail(request, booking_id):
    """ A view to show individual booking details """

    booking = get_object_or_404(Booking, pk=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'bookings/booking_detail.html', context)
