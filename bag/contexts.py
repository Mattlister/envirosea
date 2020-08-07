from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    delivery = 0
    free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD
    bag_items = []
    booking_items = []
    bag_total = 0
    booking_total = 0
    product_count = 0
    booking_count = 0
    bag = request.session.get('bag', {})
    booking = request.session.get('book', {})

    # Your Loop For Products
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            bag_total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                bag_total += item_data * product.price
                product_count += item_data
                bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                    })

        if bag_total < settings.FREE_DELIVERY_THRESHOLD:
            delivery = bag_total * \
                Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - bag_total
        else:
            delivery = 0
            free_delivery_delta = 0

        # YOUR LOOP FOR SERVICES GOES HERE

    for item_id, item_data in booking.items():
        if isinstance(item_data, int):
            booking = get_object_or_404(Booking, pk=item_id)
            booking_total += item_data * Booking.price
            booking_count += item_data
            booking_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'booking': booking,
                })
        else:
            booking = get_object_or_404(booking, pk=item_id)

        if bag_total < settings.FREE_DELIVERY_THRESHOLD:
            delivery = bag_total * \
                Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - booking_total
        # you can get rid of the else here
        # else:

    context = {
        'booking_items': booking_items,
        'booking_count': booking_count,
        'booking_total': booking_total,
        'bag_items': bag_items,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }

    return context
