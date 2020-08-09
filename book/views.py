from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from bookings.models import Booking
# Create your views here.


def view_book(request):
    """ A view that adds people to booking """

    return render(request, 'book/book.html')


def add_person(request, item_id):

    """ Add a quantity of people to the booking """
    booking = get_object_or_404(Booking, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    book = request.session.get('book', {})

    if 'booking_person' in request.POST:
        person = request.POST['booking_person']
        book = request.session.get('bag', {})

    if person:
        if item_id in list(book.keys()):
            if person in book[item_id]['items_by_person'].keys():
                book[item_id]['items_by_person'][person] += quantity
                messages.success(request, f'Updated person {person.upper()} {booking.name} quantity to {book[item_id]["items_by_person"][person]}')
            else:
                book[item_id]['items_by_person'][person] = quantity
                messages.success(request, f'Added person {person.upper()} {booking.name} to your book')
        else:
            book[item_id] = {'items_by_person': {person: quantity}}
            messages.success(request, f'Added person {person.upper()} {booking.name} to your book')
    else:
        if item_id in list(book.keys()):
            book[item_id] += quantity
            messages.success(request, f'Updated {booking.name} quantity to {book[item_id]}')
        else:
            book[item_id] = quantity
            messages.success(request, f'Added {booking.name} to your book')

    request.session['book'] = book
    return redirect(redirect_url)
    if item_id in list(book.keys()):
        book[item_id] += quantity
    else:
        book[item_id] = quantity

    request.session['book'] = book
    return redirect(redirect_url)
