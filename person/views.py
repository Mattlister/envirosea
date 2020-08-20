from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from bookings.models import Booking
# Create your views here.


def view_person(request):
    """ A view that adds people to booking """

    return render(request, 'person/person.html')


def add_person(request, item_id):

    """ Add a quantity of people to the booking """
    booking = get_object_or_404(Booking, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    person = request.session.get('person', {})

    if 'booking_person' in request.POST:
        person = request.POST['booking_person']
        person = request.session.get('person', {})

    if person:
        if item_id in list(person.keys()):
            if person in person[item_id]['items_by_person'].keys():
                person[item_id]['items_by_person'][person] += quantity
                messages.success(request, f'Updated person {person.upper()} {booking.name} quantity to {person[item_id]["items_by_person"][person]}')
            else:
                person[item_id]['items_by_person'][person] = quantity
                messages.success(request, f'Added person {person.upper()} {booking.name} to your person')
        else:
            person[item_id] = {'items_by_person': {person: quantity}}
            messages.success(request, f'Added person {person.upper()} {booking.name} to your person')
    else:
        if item_id in list(person.keys()):
            person[item_id] += quantity
            messages.success(request, f'Updated {booking.name} quantity to {person[item_id]}')
        else:
            person[item_id] = quantity
            messages.success(request, f'Added {booking.name} to your person')

    request.session['person'] = person
    return redirect(redirect_url)
    if item_id in list(person.keys()):
        person[item_id] += quantity
    else:
        person[item_id] = quantity
    request.session['person'] = person
    return redirect(redirect_url)
