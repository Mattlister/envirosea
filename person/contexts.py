from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from bookings.models import Booking


def person_contents(request):

    person_items = []
    total = 0
    booking_count = 0
    person = request.session.get('person', {})

    for item_id, item_data in person.items():
        if isinstance(item_data, int):
            booking = get_object_or_404(Booking, pk=item_id)
            total += item_data * booking.price
            booking_count += item_data
            person_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': booking,
            })
        else:
            booking = get_object_or_404(Booking, pk=item_id)
            for person, quantity in item_data['items_by_person'].items():
                total += item_data * booking.price
                booking_count += item_data
                person_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'booking': booking,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    else:
        delivery = 0

    booking_total = delivery + total

    context = {
        'person_items': person_items,
        'total': total,
        'booking_count': booking_count,
        'delivery': delivery,
        'booking_total': booking_total,
    }

    return context
