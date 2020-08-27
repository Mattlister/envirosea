from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Booking

# Create your views here.


def all_bookings(request):
    """ A view to show all bookings """

    bookings = Booking.objects.all()
    query = None
    trips = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                bookings = bookings.annotate(lower_name=Lower('name'))
            if sortkey == 'trips':
                sortkey = 'trips__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            bookings = bookings.order_by(sortkey)

        if 'trips' in request.GET:
            trips = request.GET['trips'].split(',')
            bookings = bookings.filter(category__name__in=trips)
            trips = trips.objects.filter(name__in=trips)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'bookings': bookings,
        'search_term': query,
        'current_trips': trips,
        'current_sorting': current_sorting,

    }

    return render(request, 'bookings/bookings.html', context)


def booking_detail(request, booking_id):
    """ A view to show individual booking details """

    booking = get_object_or_404(Booking, pk=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'bookings/booking_detail.html', context)


def add_booking_to_bag(request):
    """ Add a booking to the store """

    return render(request)


def add_booking(request, booking_id):
    """ Add a booking to the store """

    return render(request)
