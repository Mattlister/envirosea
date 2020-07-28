from django.contrib import admin
from .models import Booking, Trips


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class TripAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
# Registered models.


admin.site.register(Booking, BookingAdmin)
admin.site.register(Trips, TripAdmin)
