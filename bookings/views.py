from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Booking, Trips
from .forms import BookingForm

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


@ login_required
def add_booking(request):
    """ Add a booking to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save()
            messages.success(request, 'Successfully added Booking!')
            return redirect(reverse('booking_detail', args=[booking.id]))
        else:
            messages.error(
                request, 'Failed to add booking. Please ensure the form is valid.')
    else:
        form = BookingForm()

    template = 'bookings/add_booking.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_booking(request, booking_id):
    """ Edit a booking in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated booking!')
            return redirect(reverse('booking_detail', args=[booking.id]))
        else:
            messages.error(
                request, 'Failed to update booking. Please ensure the form is valid.')
    else:
        form = BookingForm(instance=booking)
        messages.info(request, f'You are editing {booking.name}')

    template = 'bookings/edit_booking.html'
    context = {
        'form': form,
        'booking': booking,
    }

    return render(request, template, context)


@login_required
def delete_booking(request, booking_id):
    """ Delete a booking from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    booking = get_object_or_404(Booking, pk=booking_id)
    booking.delete()
    messages.success(request, 'Booking deleted!')
    return redirect(reverse('bookings'))
